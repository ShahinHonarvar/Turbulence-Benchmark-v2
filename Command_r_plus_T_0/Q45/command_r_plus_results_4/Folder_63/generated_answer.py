def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:4] if c.isalpha())).lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            palindrome = letters[j:j + i]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes