def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    combinations = []
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            combinations.append(''.join(letters[i:j + 1]))
    palindromes = set()
    for word in combinations:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes