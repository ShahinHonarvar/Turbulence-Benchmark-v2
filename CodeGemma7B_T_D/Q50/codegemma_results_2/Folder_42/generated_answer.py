def if_contains_anagrams(strings):
    pairs = 0
    for i in strings:
        for j in strings:
            if i != j and sorted(i.lower()) == sorted(j.lower()) and (len(i) >= 3) and (len(j) >= 3):
                pairs += 1
    return pairs >= 233