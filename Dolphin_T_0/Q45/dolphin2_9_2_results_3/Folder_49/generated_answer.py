def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        palindromes.add(letters[i])
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1]
            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                palindromes.add(''.join(palindrome))
    return palindromes