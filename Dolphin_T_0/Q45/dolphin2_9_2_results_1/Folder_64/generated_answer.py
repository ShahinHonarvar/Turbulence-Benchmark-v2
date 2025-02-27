def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = sorted(letters[i:i + length])
            palindrome = ''.join(substring + substring[::-1])
            palindromes.add(palindrome)
    return palindromes