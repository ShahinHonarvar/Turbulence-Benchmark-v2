def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 69
    result = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result