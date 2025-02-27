def palindromes_between_indices(s):
    s = s[2:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters) + 1):
                    for m in range(l - 1, j, -1):
                        palindrome = ''.join(letters[i:l] + letters[m:k:-1])
                        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes