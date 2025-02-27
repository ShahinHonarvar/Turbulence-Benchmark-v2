def palindromes_between_indices(text):
    letters = text[2:6]
    letters = ''.join([letter for letter in letters if letter.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 4:
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring[:])
    return palindromes