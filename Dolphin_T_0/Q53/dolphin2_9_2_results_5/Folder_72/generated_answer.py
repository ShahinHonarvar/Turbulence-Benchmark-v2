def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s)):
            subs = s[i:j + 1].lower()
            if subs == subs[::-1]:
                result.add(subs)
    return result