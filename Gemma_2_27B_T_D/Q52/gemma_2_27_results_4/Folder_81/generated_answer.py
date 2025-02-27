def palindrome_of_length_n(s):
    ps = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99].lower()
        if substring == substring[::-1] and substring.isalpha():
            ps.add(substring)
    return ps