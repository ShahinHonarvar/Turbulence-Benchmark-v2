def palindromes_between_indices(s):
    valid_chars = set((c.lower() for c in s[2:10] if c.isalpha()))
    palindromes = set()
    for length in range(6, len(valid_chars) + 1):
        for i in range(len(valid_chars) - length + 1):
            palindrome = ''.join(sorted(valid_chars)[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes