def if_contains_anagrams(lst):
    anagrams_count = 0
    seen = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
    for count in seen.values():
        anagrams_count += count * (count - 1) // 2
    return anagrams_count <= 65