def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 97):
        for j in range(i, 97):
            subs = s[i:j + 1]
            if 45 <= len(subs) <= 52:
                subs = ''.join(filter(str.isalpha, subs))
                if subs.lower() == subs.lower()[::-1]:
                    result.add(subs.lower())
    return result