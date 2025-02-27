def if_contains_anagrams(strings):
    anagram_map = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagram_map:
                count += anagram_map[sorted_s]
                anagram_map[sorted_s] += 1
            else:
                anagram_map[sorted_s] = 1
            if count >= 11:
                return True
    return False