def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s in anagram_dict:
                anagram_count += 1
                if anagram_count > 84:
                    return False
            else:
                anagram_dict[sorted_s] = 1
    return True