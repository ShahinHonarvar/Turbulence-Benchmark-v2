def palindromes_between_indices(text):
    letters = text[5:7]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1]
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower() and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes