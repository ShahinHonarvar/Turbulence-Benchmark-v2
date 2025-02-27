def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1]:
            result.add(substring)
    return result