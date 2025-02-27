def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    result = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1]:
            result.add(substring)
    return result