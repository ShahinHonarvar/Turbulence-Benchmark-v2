def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                pairs += 1
    return pairs >= 5