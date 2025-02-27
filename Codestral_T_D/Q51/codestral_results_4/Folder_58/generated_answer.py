def if_contains_anagrams(strings):
    anagram_groups = []
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) < 3:
            continue
        for group in anagram_groups:
            if sorted(group[0].lower()) == sorted_s:
                group.append(s)
                break
        else:
            anagram_groups.append([s])
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups))
    return anagram_pairs <= 60