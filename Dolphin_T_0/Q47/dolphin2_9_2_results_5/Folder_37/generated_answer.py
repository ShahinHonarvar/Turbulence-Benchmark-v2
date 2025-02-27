def palindromes_of_specific_lengths(s):
    s = s[:10]
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            subs = s[i:j].lower()
            if len(subs) in range(3, 6) and subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result