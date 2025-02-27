def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 63):
        substr = s[i:i + 64]
        if substr == substr[::-1]:
            result.add(substr)
    return result