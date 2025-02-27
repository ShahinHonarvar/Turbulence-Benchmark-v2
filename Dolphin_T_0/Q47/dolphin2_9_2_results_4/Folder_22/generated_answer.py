def palindromes_of_specific_lengths(s):
    s = s[100:201]
    result = set()
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs[::-1].lower() and all((c.isalpha() for c in subs)):
                result.add(subs)
    return result