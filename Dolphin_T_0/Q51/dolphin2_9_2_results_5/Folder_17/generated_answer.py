def if_contains_anagrams(s):
    a = [''.join(sorted(i.lower())) for i in s]
    l = []
    ans = 0
    i = 0
    while i < len(a):
        if l.count(a[i]) == 0:
            l.append(a[i])
            j = i + 1
            while j < len(a):
                if a[i] == a[j]:
                    ans += 1
                    l.append(a[j])
                j += 1
            i += 1
        else:
            i += 1
    return ans < 23