from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            anagram_map[sorted_word].append(lower_word)
    anagram_count = sum((len(words) * (len(words) - 1) // 2 for words in anagram_map.values()))
    return anagram_count >= 84