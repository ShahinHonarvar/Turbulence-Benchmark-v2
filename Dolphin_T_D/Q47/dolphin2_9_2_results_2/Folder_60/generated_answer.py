def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:83]
    for length in range(32, 35):
        for i in range(0, len(substring) - length + 1):
            subs = substring[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs.lower())
    return result