def all_substring_of_size_n(s):
    if len(set(s)) < 93:
        return []
    elif len(s) < 93:
        return []
    else:
        sub = [s[i:i + 93] for i in range(len(s) - 92)]
        sub = [''.join(sorted(i)) for i in sub]
        li = list(set(sub))
        li.sort()
        return li