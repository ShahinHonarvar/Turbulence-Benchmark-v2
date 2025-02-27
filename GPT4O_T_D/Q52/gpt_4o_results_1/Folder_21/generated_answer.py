def palindrome_of_length_n(s):
    normalized_s = ''.join(filter(str.isalpha, s)).lower()
    n = 407
    result = set()
    for i in range(len(normalized_s) - n + 1):
        substring = normalized_s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result