def palindromes_of_specific_lengths(s):
    subs = s[0:5]
    subs = ''.join((c for c in subs if c.isalpha()))
    subs = subs.lower()
    subs = ''.join((c for c in subs if c in 'abcdefghijklmnopqrstuvwxyz'))
    palindromes = set()
    for start in range(len(subs)):
        for end in range(start + 2, len(subs) + 1):
            sub = subs[start:end]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes