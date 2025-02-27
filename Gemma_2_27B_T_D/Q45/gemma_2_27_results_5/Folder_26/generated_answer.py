def palindromes_between_indices(text):
    sub_string = text[4:7]
    letters = [letter for letter in sub_string if letter.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring.lower() == substring[::-1].lower() and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes