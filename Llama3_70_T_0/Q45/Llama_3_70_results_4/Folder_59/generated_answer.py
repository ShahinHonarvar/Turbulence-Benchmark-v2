def palindromes_between_indices(s):
    s = s[8:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters) + 1):
                for p in range(k - j):
                    palindrome = letters[i] + letters[j:p + j] + letters[j + p] + letters[i]
                    if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes