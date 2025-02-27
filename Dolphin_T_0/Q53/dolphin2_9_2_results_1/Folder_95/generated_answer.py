def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(35, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            subs = s[j:j + i]
            if subs == subs[::-1]:
                result.add(subs)
    return result