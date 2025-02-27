def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        sorted_str = ''.join(sorted(lst[i].lower()))
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            sorted_str_2 = ''.join(sorted(lst[j].lower()))
            if sorted_str == sorted_str_2:
                anagram_pairs.add((i, j))
                anagram_count += 1
    return anagram_count <= 2