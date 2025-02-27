from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_dict = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs_count = sum((1 for words in anagram_dict.values() if len(words) >= 2 and len(words[0]) >= 3))
    return anagram_pairs_count >= 30