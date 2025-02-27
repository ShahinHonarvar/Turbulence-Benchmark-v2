def find_original_set(a, b, c, d, e, f, g):
    ans = a
    for s in [b, c, d, e, f, g]:
        if s <= ans:
            ans = s
    return ans