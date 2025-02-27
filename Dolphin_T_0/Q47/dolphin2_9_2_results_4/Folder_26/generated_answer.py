def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(24, 85):
        for j in range(i + 21, min(i + 32, 85)):
            subs = s[i:j].lower()
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result