def all_substring_of_size_n(s):
    n = 30
    result = []
    s = s + ' '
    l = len(s)
    for i in range(l - n + 1):
        subs = s[i:i + n]
        flag = True
        for j in range(len(subs) - 1):
            for k in range(j + 1, len(subs)):
                if subs[j] == subs[k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            result.append(subs)
    return result