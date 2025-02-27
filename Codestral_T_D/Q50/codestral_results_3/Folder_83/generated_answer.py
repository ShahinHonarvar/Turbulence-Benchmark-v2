def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(lower_s)
            else:
                anagram_dict[sorted_s] = [lower_s]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 48