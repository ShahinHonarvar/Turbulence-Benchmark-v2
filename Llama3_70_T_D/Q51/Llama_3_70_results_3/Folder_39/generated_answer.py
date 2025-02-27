def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagram_count:
            anagram_count[s_sorted] += 1
        else:
            anagram_count[s_sorted] = 1
    anagram_pairs = sum([count * (count - 1) // 2 for count in anagram_count.values()])
    return anagram_pairs <= 257