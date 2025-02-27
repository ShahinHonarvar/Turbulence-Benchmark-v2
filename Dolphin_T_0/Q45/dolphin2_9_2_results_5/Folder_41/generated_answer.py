def palindromes_between_indices(s):
    sub_s = s[2:4]
    set_pal = set()
    for p in range(3, len(sub_s) + 1):
        for i in range(len(sub_s) - p + 1):
            subs = sub_s[i:i + p]
            if subs == subs[::-1]:
                set_pal.add(subs.lower())
    return set_pal