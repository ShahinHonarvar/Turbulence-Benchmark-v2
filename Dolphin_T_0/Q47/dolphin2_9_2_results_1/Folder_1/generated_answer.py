def palindromes_of_specific_lengths(s):
    s = s[15:90]
    result = set()
    for length in range(40, 73):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length].lower()
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result