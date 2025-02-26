def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = 57
    result = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substr = s[i:j + 1]
            if substr == substr[::-1]:
                result.add(substr)
    return result