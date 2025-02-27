def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10]))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes