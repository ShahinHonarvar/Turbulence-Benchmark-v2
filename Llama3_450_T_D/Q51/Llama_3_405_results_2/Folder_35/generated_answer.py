def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_dict:
            count += anagram_dict[sorted_str]
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    return count <= 210