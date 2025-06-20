def palindromes_of_specific_lengths(s):
    s = s[20:63]
    result = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs.lower())
    return result