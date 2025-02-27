def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s] = anagram_dict.get(sorted_s, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs <= 52