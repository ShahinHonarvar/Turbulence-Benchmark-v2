def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9):
    d = {}
    for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9]:
        for x in s:
            d[x] = True
    return {x for x in range(1, 10) if d[x]}