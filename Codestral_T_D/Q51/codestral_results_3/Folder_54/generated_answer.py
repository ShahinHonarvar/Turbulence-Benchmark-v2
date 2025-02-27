def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
        if anagram_dict[sorted_s] == 2:
            anagram_count += 1
        if anagram_count > 39:
            return False
    return True