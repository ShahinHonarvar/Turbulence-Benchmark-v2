def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    if len(s) > 50:
        s = s[0:50]
    pal = set()
    for length in range(50, 101):
        for i in range(len(s)):
            if i + length <= len(s):
                subs = s[i:length + i]
                subs = ''.join(filter(str.isalpha, subs))
                subs = subs.lower()
                if subs == subs[::-1]:
                    pal.add(subs)
    return pal