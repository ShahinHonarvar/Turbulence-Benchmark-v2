def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        lower = word.lower()
        sorted_lower = ''.join(sorted(lower))
        if sorted_lower in seen:
            count += 1
        else:
            seen.add(sorted_lower)
    return count <= 289