def palindromes_between_indices(text):
    letters = ''.join([c for c in text[1:5] if c.isalpha()]).lower()
    palindromes = set()
    for i in range(len(letters) // 2):
        for j in range(i + 1, len(letters) // 2 + 1):
            substring = letters[i:j]
            reversed_substring = substring[::-1]
            if substring == reversed_substring and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes