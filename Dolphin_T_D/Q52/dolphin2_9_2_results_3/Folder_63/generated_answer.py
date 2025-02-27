def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 17):
        subs = s[i:i + 18]
        if subs == subs[::-1] and subs.isalpha():
            result.add(subs)
    return result