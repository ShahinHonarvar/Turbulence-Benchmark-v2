def if_contains_anagrams(strings):
    count = 0
    for pair in zip(strings, strings[1:]):
        s1, s2 = pair
        if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())):
            count += 1
    return count <= 10