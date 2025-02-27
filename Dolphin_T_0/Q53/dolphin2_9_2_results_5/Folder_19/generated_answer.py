def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 22):
        for j in range(i + 23, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result