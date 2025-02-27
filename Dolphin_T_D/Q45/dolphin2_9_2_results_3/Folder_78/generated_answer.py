def palindromes_between_indices(s):
    letters = s[6:9]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if len(sub) >= 3 and sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes