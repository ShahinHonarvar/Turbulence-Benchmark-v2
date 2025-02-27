def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 3:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count >= 81