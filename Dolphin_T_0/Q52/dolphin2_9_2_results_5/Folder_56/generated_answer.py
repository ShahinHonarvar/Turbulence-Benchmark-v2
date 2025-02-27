def palindrome_of_length_n(s):
    s = s.lower()
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 95, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                substrings.add(substring)
    return substrings