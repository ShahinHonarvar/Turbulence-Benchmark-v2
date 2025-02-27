from collections import defaultdict

def if_contains_anagrams(words):
    sorted_words = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_words[sorted_word].append(word)
    anagram_count = 0
    for word_list in sorted_words.values():
        if len(word_list[0]) >= 3:
            anagram_count += len(word_list) * (len(word_list) - 1) // 2
    return anagram_count >= 178