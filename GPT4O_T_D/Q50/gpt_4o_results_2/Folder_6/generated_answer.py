def if_contains_anagrams(strings):
    count = 0
    seen = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in seen:
                count += seen[sorted_s]
                seen[sorted_s] += 1
            else:
                seen[sorted_s] = 1
        if count >= 26:
            return True
    return False