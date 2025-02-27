def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if substring == substring[::-1]:
            result.add(substring)
    return result