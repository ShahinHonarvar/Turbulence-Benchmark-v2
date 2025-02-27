def all_substring_of_size_n(s):
    if len(s) < 32:
        return []
    out = set()
    for i in range(len(s) - 31):
        tmp = ''
        for j in range(i, i + 32):
            if s[j] in tmp:
                break
            else:
                tmp += s[j]
        else:
            out.add(tmp)
    return list(out)