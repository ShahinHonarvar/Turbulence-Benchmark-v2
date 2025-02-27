def palindrome_of_length_n(s):
    palindrome = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                for k in range(j + 1, len(s)):
                    if s[i] == s[k]:
                        palindrome.add(s[i:k + 1])
    return palindrome