def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 37, n):
            subs = s[i:j + 1]
            if subs == subs[::-1]:
                result.add(subs)
    return result