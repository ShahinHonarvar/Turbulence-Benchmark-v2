def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 26:
                result.add(s[i:j])
    return result