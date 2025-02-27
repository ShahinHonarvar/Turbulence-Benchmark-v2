def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(''.join(palindrome))
    return palindromes