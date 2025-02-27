def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes