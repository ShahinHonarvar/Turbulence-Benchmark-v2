def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            for k in range(j, len(s) + 1):
                for l in range(k, len(s) + 1):
                    if s[i:j] == s[l:k][::-1] and len(s[i:j]) + len(s[l:k]) >= 4:
                        palindrome = s[i:j] + s[l:k]
                        palindromes.add(palindrome)
    return palindromes