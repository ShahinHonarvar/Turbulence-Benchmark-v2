def palindromes_between_indices(string):
    substring = string[4:8]
    letters = ''.join([char for char in substring if char.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters)):
            sub = letters[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes