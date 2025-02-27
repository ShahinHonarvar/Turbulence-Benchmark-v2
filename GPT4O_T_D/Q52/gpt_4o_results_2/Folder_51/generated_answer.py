def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 73:
        return result
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if substring == substring[::-1]:
            result.add(substring)
    return result