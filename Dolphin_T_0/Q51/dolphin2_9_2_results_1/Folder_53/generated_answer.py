def if_contains_anagrams(lst):
    count = 0
    pairs = set()
    for word in lst:
        lower = word.lower()
        if len(lower) >= 3:
            key = ''.join(sorted(lower))
            pairs.add(key)
            if key in pairs:
                count += 1
    if count >= 8:
        return True
    return False