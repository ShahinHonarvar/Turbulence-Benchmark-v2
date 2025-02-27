def palindromes_between_indices(text):
    letters = sorted([c for c in text[:4].lower() if c.isalpha()])
    palindromes = set()
    for i in range(len(letters) // 2):
        for j in range(i + 1, len(letters) // 2 + 1):
            palindrome = ''.join(letters[:i] + letters[i:j][::-1] + letters[:i])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes