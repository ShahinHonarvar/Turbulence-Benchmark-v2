def palindromes_between_indices(text):
    palindromes = set()
    for i in range(5):
        for j in range(i + 1, 7):
            letters = text[i:j + 1]
            if letters == letters[::-1]:
                palindromes.add(letters)
    return palindromes