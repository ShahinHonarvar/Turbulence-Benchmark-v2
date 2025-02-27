def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    n = 14
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == ''.join(reversed(sub)) and sub.isalpha():
                result.add(sub)
    return result