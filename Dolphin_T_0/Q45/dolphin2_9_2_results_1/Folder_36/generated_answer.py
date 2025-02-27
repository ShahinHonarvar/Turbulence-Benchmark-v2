def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[5:9]))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes