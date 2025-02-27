def palindromes_between_indices(string):
    letters = []
    for i in range(6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(j + 1, len(letters) + 1):
                word = letters[i:j] + letters[j:k] + letters[i:j][::-1]
                if len(word) >= 3:
                    result.add(''.join(word))
    return result