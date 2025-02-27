def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    for start in range(len(s)):
        for end in range(start + 52, len(s) + 1):
            substring = s[start:end].lower()
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set