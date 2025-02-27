def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if s_lower not in anagram_dict and len(s) >= 3:
            anagram_dict[s_lower] = [sorted_str]
        elif len(s) >= 3:
            if sorted_str in anagram_dict[s_lower]:
                count += 1
            else:
                anagram_dict[s_lower].append(sorted_str)
    return count >= 49