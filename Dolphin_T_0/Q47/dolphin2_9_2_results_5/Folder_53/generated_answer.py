def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:300]
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs.lower())
    return result