from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if len(key) < 3:
            continue
        anagram_dict[key].append(word)
    num_anagrams = sum((len(group) for group in anagram_dict.values() if len(group) >= 2))
    return num_anagrams <= 289