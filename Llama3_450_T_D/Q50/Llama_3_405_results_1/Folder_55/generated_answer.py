def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values() if len(value) > 1))
    return count >= 15