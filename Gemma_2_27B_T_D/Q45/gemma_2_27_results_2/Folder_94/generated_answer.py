def palindromes_between_indices(text):
    letters = text[3:5].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1]
            reversed_substring = substring[::-1]
            if substring == reversed_substring and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes