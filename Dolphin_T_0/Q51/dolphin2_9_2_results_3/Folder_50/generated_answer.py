def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in seen:
                count += 1
            else:
                seen.add(sorted_s)
    return count <= 47