from collections import defaultdict

def if_contains_anagrams(words):
    sorted_words = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_words[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in sorted_words.values():
        if len(word_list[0]) >= 3 and len(word_list) > 1:
            anagram_pairs += len(word_list) - 1
    return anagram_pairs <= 5