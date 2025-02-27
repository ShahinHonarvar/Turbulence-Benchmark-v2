def palindromes_between_indices(s):
    s = s[3:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes