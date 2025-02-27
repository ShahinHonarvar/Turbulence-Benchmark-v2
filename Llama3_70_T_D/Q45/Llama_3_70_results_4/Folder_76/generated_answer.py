def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            for k in range(len(s), j - 1, -1):
                for last in range(k - 1, j - 1, -1):
                    if (i == 0 or s[i - 1].isalpha()) and s[j - 1].isalpha() and s[k - 1].isalpha() and (last == len(s) - 1 or s[last + 1].isalpha()):
                        palindrome = s[i:j] + s[k - 1:last:-1]
                        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes