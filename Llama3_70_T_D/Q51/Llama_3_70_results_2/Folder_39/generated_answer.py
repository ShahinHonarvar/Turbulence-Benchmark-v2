def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_count:
            anagram_count[sorted_str] += 1
        else:
            anagram_count[sorted_str] = 1
    count = 0
    for k in anagram_count:
        count += anagram_count[k] * (anagram_count[k] - 1) // 2
    return count <= 257