def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        sorted_str = ''.join(sorted(lst[i].lower()))
        if sorted_str not in anagram_set:
            anagram_set.add(sorted_str)
        else:
            anagram_count += 1
    return anagram_count >= 54 and len(anagram_set) >= 54