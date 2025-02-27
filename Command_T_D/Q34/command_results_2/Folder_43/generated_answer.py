def find_original_set(s):
    if len(s) == 1:
        return s[0]
    s = sorted(s)
    return {*min(s, key=len)}