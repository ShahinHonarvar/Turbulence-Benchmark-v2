def all_substring_of_size_n(s):
    if len(set(s)) < 54:
        return []
    subs = set()
    for i in range(len(s)):
        for j in range(i + 54, len(s) + 1):
            subs.add(s[i:j])
    return [s for s in subs if len(set(s)) == 54]