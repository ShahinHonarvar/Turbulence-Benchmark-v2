from collections import Counter

def if_contains_anagrams(words):
    anagrams = 0
    words_set = set(words)
    for word in words_set:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams += len(words_set & set(filter(sorted_word.__eq__, words_set))) - 1
    return anagrams >= 59