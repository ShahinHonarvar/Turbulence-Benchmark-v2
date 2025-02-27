def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 150
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= n:
                palindrome_set.add(substring)
    return palindrome_set