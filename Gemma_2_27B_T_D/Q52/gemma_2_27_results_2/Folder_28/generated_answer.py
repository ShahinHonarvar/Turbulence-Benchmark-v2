def palindrome_of_length_n(s):
    p = set()
    for i in range(len(s) - 42):
        substring = s[i:i + 43].lower()
        if substring == substring[::-1] and substring.isalpha():
            p.add(substring)
    return p