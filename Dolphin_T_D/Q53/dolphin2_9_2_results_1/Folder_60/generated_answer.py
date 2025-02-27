def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 79, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set