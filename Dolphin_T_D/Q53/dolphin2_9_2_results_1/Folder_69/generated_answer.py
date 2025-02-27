def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 97):
        for j in range(i + 1, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result