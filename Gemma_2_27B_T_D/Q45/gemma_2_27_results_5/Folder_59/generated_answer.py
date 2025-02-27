def palindromes_between_indices(text):
    substring = text[8:10]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            word = ''.join(letters[i:j + 1]).lower()
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes