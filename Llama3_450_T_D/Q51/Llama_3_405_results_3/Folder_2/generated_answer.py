def if_contains_anagrams(string_list):
    anagram_count = {}
    for s in string_list:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_count:
            anagram_count[sorted_str] += 1
        else:
            anagram_count[sorted_str] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagram_count.values()))
    return pairs <= 81