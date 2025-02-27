def palindromes_between_indices(string):
    s = string[4:10].lower()
    letters = [ch for ch in s if ch.isalpha()]
    results = set()
    if len(letters) < 5:
        return results
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters) + 1):
            word = letters[i:j]
            if word == word[::-1]:
                results.add(''.join(word))
    return results