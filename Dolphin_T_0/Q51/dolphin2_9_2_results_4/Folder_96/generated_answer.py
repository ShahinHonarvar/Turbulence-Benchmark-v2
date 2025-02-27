def if_contains_anagrams(arr):
    count = 0
    seen = set()
    for s in arr:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in seen:
                count += 1
                if count > 2:
                    return False
            else:
                seen.add(sorted_s)
    return True