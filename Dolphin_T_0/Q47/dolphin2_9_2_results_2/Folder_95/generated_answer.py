def palindromes_of_specific_lengths(s):
    s = s[11:57]
    result = set()
    for i in range(len(s) - 20 + 1):
        subs = s[i:i + 21]
        if subs == subs[::-1] and subs.isalpha():
            result.add(subs.lower())
    return result