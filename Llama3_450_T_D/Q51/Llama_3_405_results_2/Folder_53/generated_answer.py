def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count > 8:
            return False
    return True