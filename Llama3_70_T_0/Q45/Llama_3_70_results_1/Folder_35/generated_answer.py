def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            for k in range(len(s), j - 1, -1):
                for l in range(k - 1, i - 1, -1):
                    palindrome = s[i:j] + s[k:l + 1]
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes