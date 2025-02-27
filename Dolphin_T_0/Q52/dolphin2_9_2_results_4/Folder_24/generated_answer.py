def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 29, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                result.add(subs)
    return result