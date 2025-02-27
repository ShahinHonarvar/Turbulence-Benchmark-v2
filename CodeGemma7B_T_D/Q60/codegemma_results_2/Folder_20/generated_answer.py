def all_left_right_truncatable_prime(t):
    if t[100] < 20:
        return []
    pn = [2, 3, 5, 7, 11, 13, 17, 19]
    suffixes = {pn[i]: set((str(j) for j in pn if str(j)[-1] in str(pn[i]) and str(j)[-1] != str(pn[i])[0] and (j != pn[i]))) for i in range(8)}
    not_prime = {i: set() for i in range(10)}
    not_prime[0] = {s for s in suffixes.values() if len(s) == 1}
    for i in range(10):
        for s in suffixes:
            suffixes[s].difference_update(not_prime[i])
        for j in set((j for suffix in suffixes for j in suffix)):
            candidate = int(str(j) + str(i))
            if candidate in pn:
                suffixes[j].add(str(i))
            elif candidate % 2 == 0 or candidate % 3 == 0:
                not_prime[i].add(str(j))
    prefixes_dict = {i: set((str(j) for j in pn if str(j)[-1] in suffix and int(str(j)[:2]) % 2 == 1 and (int(str(j)[:2]) % 3 == 1) if len(str(j)) > 2)) for i, suffix in suffixes.items()}
    for i in range(10):
        for j in prefixes_dict:
            prefixes_dict[j].difference_update(not_prime[i])
    candidates = []
    for i in range(2, t[100] + 1):
        s = str(i)
        if s[0] == '0' or s[-1] == '0' or s[-1] == s[0]:
            continue
        if len(s) < 2 or int(s[:2]) % 2 == 0 or int(s[:2]) % 3 == 0:
            continue
        if s in suffixes[int(s[-1])]:
            if s[:-1] in prefixes_dict[int(s[-1])]:
                candidates.append(i)
    return sorted(candidates, reverse=True)