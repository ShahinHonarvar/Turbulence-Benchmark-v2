def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagram_dict:
                count += anagram_dict[sorted_s]
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    return count >= 75