def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    result = set()
    for i in range(24, 53):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            if subs == subs[::-1]:
                if subs.isalpha():
                    result.add(subs)
    return result