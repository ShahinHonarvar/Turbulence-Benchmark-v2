def if_contains_anagrams(strings):
    count = 0
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                count += 1
                if count > 61:
                    return False
            else:
                anagram_dict[sorted_s] = 1
    return True