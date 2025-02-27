from collections import defaultdict

def if_contains_anagrams(strings):
    counter = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    for anagrams in anagram_dict.values():
        valid_anagrams = [a for a in anagrams if len(a) >= 3]
        pair_count = len(valid_anagrams) * (len(valid_anagrams) - 1) // 2
        counter += pair_count
        if counter > 181:
            return False
    return True