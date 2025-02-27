from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = [group for group in anagram_dict.values() if len(group) > 1 and len(group[0]) >= 3]
    return len(anagram_pairs) <= 10