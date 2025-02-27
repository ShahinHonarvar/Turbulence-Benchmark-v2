def palindromes_of_specific_lengths(s):
    s = s[1:8]
    result = set()
    for i in range(3, 5):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result