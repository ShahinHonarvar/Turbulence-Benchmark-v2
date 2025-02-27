def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s in anagram_dict:
                count += anagram_dict[sorted_s]
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    return count >= 49