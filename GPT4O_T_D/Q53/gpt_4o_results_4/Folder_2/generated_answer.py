def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 55, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result