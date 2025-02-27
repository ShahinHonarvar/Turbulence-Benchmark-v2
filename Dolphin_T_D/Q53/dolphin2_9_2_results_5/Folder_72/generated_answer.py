def palindrome_of_length_at_least_n(s):
    result = set()
    n = 88
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                result.add(subs)
    return result