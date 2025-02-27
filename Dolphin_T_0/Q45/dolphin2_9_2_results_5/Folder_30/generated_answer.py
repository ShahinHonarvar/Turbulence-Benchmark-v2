def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:5])).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes