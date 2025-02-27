from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for key in anagram_dict:
        words = anagram_dict[key]
        if len(words) >= 2 and len(key) >= 3:
            anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs <= 59