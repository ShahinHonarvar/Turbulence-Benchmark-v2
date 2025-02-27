def if_contains_anagrams(s):
    ans = 0
    seen = {}
    for word in s:
        if len(word) >= 3:
            t = ''.join(sorted(word.lower()))
            if t in seen:
                ans += 1
            else:
                seen[t] = 1
    return ans >= 17