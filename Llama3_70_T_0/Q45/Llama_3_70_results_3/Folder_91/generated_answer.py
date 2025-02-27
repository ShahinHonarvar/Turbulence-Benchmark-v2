def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring)):
                palindrome = substring[:k] + substring[k:].reverse()
                palindrome = ''.join(palindrome)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes