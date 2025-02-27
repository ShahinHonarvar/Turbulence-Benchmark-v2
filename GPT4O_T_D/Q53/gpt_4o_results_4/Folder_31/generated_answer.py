def palindrome_of_length_at_least_n(s):
    n = 34
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result