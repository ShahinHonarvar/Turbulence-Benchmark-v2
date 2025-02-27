def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        wa = ''.join(sorted(word.lower()))
        if wa in seen:
            count += 1
        seen.add(wa)
    return count <= 25