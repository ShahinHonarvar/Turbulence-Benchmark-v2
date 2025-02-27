def if_contains_anagrams(s):
    ans = 0
    new = {}
    for i in range(len(s)):
        sorted_s = ''.join(sorted(s[i].lower()))
        if sorted_s not in new:
            new[sorted_s] = [s[i]]
        else:
            new[sorted_s].append(s[i])
    for i in list(new.values()):
        if len(set(i)) >= 1 and len(i) >= 2 and (len(set(i)) <= 10):
            ans += 1
    return ans