def palindromes_between_indices(s):
    s = s[3:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters) + 1):
                    for m in range(l - 1, j - 1, -1):
                        for n in range(m - 1, i - 1, -1):
                            palindrome = letters[i] + letters[j] + letters[k] + letters[l - 1] + letters[m] + letters[n]
                            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    return palindromes