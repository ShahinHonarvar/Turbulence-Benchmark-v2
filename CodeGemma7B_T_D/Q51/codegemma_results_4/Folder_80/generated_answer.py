def if_contains_anagrams(str_list):
    anagram_counts = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and sorted_s not in anagram_counts:
            anagram_counts[sorted_s] = 0
        if len(sorted_s) >= 3 and sorted_s in anagram_counts:
            anagram_counts[sorted_s] += 1
    if sum(anagram_counts.values()) <= 255:
        return True
    else:
        return False