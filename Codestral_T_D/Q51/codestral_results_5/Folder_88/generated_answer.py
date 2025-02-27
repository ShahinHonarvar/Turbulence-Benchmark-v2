def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in anagram_dict:
                anagram_count += len(anagram_dict[sorted_s])
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    return anagram_count <= 407