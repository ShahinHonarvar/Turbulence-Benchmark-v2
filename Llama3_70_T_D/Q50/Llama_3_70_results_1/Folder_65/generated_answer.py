def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_list = [''.join(sorted(s.casefold())) for s in lst if len(s) >= 3]
    for s in sorted_list:
        if sorted_list.count(s) > 1:
            anagram_count += sorted_list.count(s) - 1
    return anagram_count >= 94