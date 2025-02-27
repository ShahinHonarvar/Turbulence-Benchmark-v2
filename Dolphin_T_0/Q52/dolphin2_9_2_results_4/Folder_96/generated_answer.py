def palindrome_of_length_n(s):
    s = s.lower()
    length = 83
    palindrome_set = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set