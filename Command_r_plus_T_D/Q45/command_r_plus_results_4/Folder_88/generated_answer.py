def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes