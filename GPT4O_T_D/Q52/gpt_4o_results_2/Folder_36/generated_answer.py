def palindrome_of_length_n(s):
    target_length = 338
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            result.add(substring)
    return result