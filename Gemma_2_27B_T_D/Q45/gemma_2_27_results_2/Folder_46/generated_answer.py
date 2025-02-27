def palindromes_between_indices(text):
    letters = sorted([c for c in text[4:10] if c.isalpha()])
    palindromes = set()
    if len(letters) >= 6:
        for i in range(len(letters) - 5):
            for j in range(i + 6, len(letters) + 1):
                substring = ''.join(letters[i:j])
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes