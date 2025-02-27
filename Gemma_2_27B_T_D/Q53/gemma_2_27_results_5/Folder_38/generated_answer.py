def palindrome_of_length_at_least_n(s):
    p = set()
    for i in range(len(s) - 55):
        for j in range(i + 55, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                p.add(substring)
    return p