def palindrome_of_length_at_least_n(s):
    s = s.lower()
    output = set()
    for i in range(len(s)):
        for j in range(i + 8, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                output.add(substring)
    return output