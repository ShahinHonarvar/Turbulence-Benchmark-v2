def if_contains_anagrams(strng):
    pairs = 0
    seen = set()
    for s in strng:
        if len(s) < 3:
            continue
        temp = ''.join(sorted([c.lower() for c in s if c.isalpha()]))
        if temp in seen:
            pairs += 1
        else:
            seen.add(temp)
    return pairs <= 65