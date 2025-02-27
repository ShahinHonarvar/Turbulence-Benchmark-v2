def palindromes_of_specific_lengths(s):
    sub_s = s[18:99]
    result = set()
    for length in range(31, 52):
        for sub in range(len(sub_s) - length + 1):
            subs = sub_s[sub:sub + length]
            if subs == subs[::-1].lower() and subs.isalpha():
                result.add(subs)
    return result