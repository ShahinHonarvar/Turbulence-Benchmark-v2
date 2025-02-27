def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            for k in range(len(s)):
                for l in range(k + 1, len(s) + 1):
                    if s[i:j] == s[k:l][::-1] and len(s[i:j]) >= 3:
                        palindrome = s[i:j] + s[k:l][::-1]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes