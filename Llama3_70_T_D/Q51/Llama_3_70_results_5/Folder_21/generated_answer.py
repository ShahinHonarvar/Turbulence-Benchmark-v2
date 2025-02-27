def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagram_count[sorted_s] = anagram_count.get(sorted_s, 0) + 1
    return sum((count - 1 for count in anagram_count.values() if count > 1)) <= 26