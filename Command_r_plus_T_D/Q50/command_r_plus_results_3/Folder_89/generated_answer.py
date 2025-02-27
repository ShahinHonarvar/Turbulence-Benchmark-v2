def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                sorted_i = sorted(lst[i].lower())
                sorted_j = sorted(lst[j].lower())
                if sorted_i == sorted_j and (lst[i], lst[j]) not in anagram_set and ((lst[j], lst[i]) not in anagram_set):
                    anagram_count += 1
                    anagram_set.add((lst[i], lst[j]))
                    if anagram_count >= 36:
                        return True
    return False