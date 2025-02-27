def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                sorted_i = sorted(lst[i].lower())
                sorted_j = sorted(lst[j].lower())
                if sorted_i == sorted_j and (lst[i], lst[j]) not in anagram_pairs and ((lst[j], lst[i]) not in anagram_pairs):
                    anagram_count += 1
                    anagram_pairs.add((lst[i], lst[j]))
                    if anagram_count == 52:
                        return True
    return False