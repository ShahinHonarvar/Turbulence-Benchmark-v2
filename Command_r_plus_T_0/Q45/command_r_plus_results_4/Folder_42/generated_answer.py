def palindromes_between_indices(s):
    letters = ''.join((c for c in s[6:10] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes