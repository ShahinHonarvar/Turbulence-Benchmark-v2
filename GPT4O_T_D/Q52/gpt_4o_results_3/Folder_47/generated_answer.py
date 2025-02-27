def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    result = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if substring == substring[::-1]:
            result.add(substring)
    return result