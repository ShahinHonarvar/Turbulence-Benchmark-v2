def palindromes_of_specific_lengths(s):
    sub = s[10:94]
    set_pals = set()
    for i in range(11, 94):
        for j in range(i + 33, min(i + 55, 94)):
            subs = sub[i:j + 1].lower()
            if subs == subs[::-1] and subs.isalpha():
                set_pals.add(subs)
    return set_pals