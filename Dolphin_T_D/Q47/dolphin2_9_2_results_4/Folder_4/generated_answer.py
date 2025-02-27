def palindromes_of_specific_lengths(s):
    sub_s = s[12:93]
    result = set()
    for length in range(17, 67):
        for i in range(len(sub_s) - length + 1):
            subs = sub_s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs.lower())
    return result