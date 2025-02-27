def if_contains_anagrams(strings):
    count = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if len(s1) < 3 or len(s2) < 3:
                continue
            if sorted(s1.lower()) == sorted(s2.lower()):
                count += 1
    return count >= 77