from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values() if len(words) >= 2))
    return anagram_pairs >= 58