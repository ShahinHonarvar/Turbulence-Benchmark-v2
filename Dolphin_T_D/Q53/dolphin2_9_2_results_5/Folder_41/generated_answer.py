def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 28
    result = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            if s[start:start + length] == s[start:start + length][::-1] and s[start:start + length].isalpha():
                result.add(s[start:start + length])
    return result