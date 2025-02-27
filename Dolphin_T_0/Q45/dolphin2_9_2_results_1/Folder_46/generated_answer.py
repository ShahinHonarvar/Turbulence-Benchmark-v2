def palindromes_between_indices(s):
    substring = s[4:10]
    letters = [c.lower() for c in substring if c.isalpha()]
    palindromes = set()
    for i in range(6, len(substring) + 1):
        for palindrome in ''.join(letters).lower()[::-1]:
            if len(palindrome) < i:
                break
            if palindrome == palindrome[::-1][:i]:
                palindromes.add(palindrome)
    return palindromes