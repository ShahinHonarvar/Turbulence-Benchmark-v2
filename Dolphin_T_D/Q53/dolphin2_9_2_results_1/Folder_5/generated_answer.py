def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 45, len(s)):
            subs = s[i:j + 1]
            if subs == subs[::-1]:
                result.add(subs)
    return result