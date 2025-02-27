def if_contains_anagrams(str_list):
    anagram_pairs = 0
    seen_str = set()
    for s in str_list:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen_str:
            anagram_pairs += 1
        seen_str.add(sorted_s)
    return anagram_pairs <= 407