def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagram_pairs.add((lst[i], lst[j]))
    return len(anagram_pairs) <= 40