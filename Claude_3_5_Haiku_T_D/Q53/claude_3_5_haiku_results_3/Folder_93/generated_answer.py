def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for length in range(90, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set