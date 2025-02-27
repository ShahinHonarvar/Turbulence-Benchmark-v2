def palindromes_between_indices(s):
    letters = s[3:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1] and len(sub) >= 3:
                palindromes.add(sub.lower())
    return palindromes