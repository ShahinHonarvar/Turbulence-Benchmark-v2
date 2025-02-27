def if_contains_anagrams(string_list):
    anagram_count = {}
    for s in string_list:
        s = ''.join((e for e in s if e.isalpha())).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_count:
            anagram_count[sorted_str] += 1
        else:
            anagram_count[sorted_str] = 1
    count = sum((1 for v in anagram_count.values() if v > 1))
    return count <= 22