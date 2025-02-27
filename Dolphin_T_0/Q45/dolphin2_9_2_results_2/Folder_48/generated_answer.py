def palindromes_between_indices(s):
    letters = ''.join(sorted(s[6:9]))
    length = len(letters)
    palindromes = set()
    for i in range(length):
        for j in range(i + 3, length):
            sub = letters[i:j + 1]
            if len(sub) >= 4 and sub == sub[::-1]:
                palindromes.add(''.join(sorted(sub)))
    return palindromes