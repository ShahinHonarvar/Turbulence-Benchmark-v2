def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = len(s)
    for i in range(length - 9):
        substr = s[i:i + 10]
        if substr == substr[::-1]:
            result.add(substr)
    return result