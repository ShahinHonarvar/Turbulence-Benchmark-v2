def if_contains_anagrams(str_list):
    """Counts number of pairs of anagrams of length >= 3"""
    seen = set()
    count = 0
    for s in str_list:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        if len(s) >= 3 and s_sorted in seen:
            count += 1
        seen.add(s_sorted)
    return count >= 276