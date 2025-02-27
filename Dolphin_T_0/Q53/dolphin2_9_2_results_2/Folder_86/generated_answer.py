def palindrome_of_length_at_least_n(s):
    s = s.lower()
    a = []
    palindrome_set = set()
    n = 133
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set