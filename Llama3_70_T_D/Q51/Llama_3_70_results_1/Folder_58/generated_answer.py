def if_contains_anagrams(strings):
    anagram_count = {}
    anagram_pairs = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_count:
            anagram_count[sorted_s] += 1
        else:
            anagram_count[sorted_s] = 1
    for count in anagram_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 60