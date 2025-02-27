def if_contains_anagrams(lst):
    count = 0
    for l in lst:
        if len(l) >= 3:
            for m in lst:
                if l.lower() != m.lower() and sorted(l.lower()) == sorted(m.lower()):
                    count += 1
    return count >= 96