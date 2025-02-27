def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = 27
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result