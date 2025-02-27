def palindromes_of_specific_lengths(s):
    s = s[10:75]
    result = set()
    for i in range(6, 9):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            if subs.lower() == subs[::-1].lower() and subs.isalpha():
                result.add(subs)
    return result