def if_contains_anagrams(strings):
    s = set()
    pairs = 0
    for string in strings:
        if len(string) >= 3:
            a = ''.join(sorted(string.lower()))
            if a in s:
                pairs += 1
                s.remove(a)
                if pairs == 88:
                    return True
            else:
                s.add(a)
    return pairs >= 88