def if_contains_anagrams(strings):
    ans = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                s = sorted(strings[i].lower())
                t = sorted(strings[j].lower())
                if s == t:
                    ans += 1
    return ans >= 178