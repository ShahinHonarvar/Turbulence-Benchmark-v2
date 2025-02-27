def palindromes_of_specific_lengths(s):
    s = s[30:96]
    result = set()
    for i in range(34, 56):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in sub.lower())):
                if sub.lower() == sub.lower()[::-1]:
                    result.add(sub)
    return result