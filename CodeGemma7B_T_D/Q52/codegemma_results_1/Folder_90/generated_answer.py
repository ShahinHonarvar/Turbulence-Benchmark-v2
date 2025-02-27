def palindrome_of_length_n(s):
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                substring = s[i:k + 1]
                if substring == substring[::-1] and len(substring) == 318 and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set