def palindromes_between_indices(s):
    str_lower = s.lower()
    l, r = (2, 5)
    ans = set()
    while r < len(str_lower):
        count = {}
        for i in range(l, r + 1):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in count:
                count[c] = 0
        for i in range(l, r + 1):
            if count[str_lower[i]] > 0:
                count[str_lower[i]] -= 1
                str_lower = str_lower[:i] + str_lower[i + 1:]
                break
        else:
            ans.add(str_lower[l:r + 1])
        l += 1
        r += 1
    return ans