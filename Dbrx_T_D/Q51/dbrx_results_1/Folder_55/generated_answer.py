import sys

def if_contains_anagrams(words):
    anagrams_count = 0
    used_words = set()
    max_word_length = 3
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= max_word_length and sorted_word not in used_words:
            used_words.add(sorted_word)
            anagrams_count += 1
        if anagrams_count > 44:
            return False
    return True