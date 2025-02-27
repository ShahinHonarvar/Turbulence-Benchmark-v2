def palindromes_between_indices(text):
    letters = [c for c in text[0:7] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if len(substring) >= 5 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes