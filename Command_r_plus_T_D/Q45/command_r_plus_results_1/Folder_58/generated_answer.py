def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:7] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters) // 2 + 1):
        for j in range(len(letters) - 2 * i + 1):
            palindrome = letters[j:j + i] + letters[j + i:j + 2 * i][::-1]
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
    return palindromes