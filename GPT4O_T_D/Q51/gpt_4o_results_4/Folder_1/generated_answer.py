from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_letters(word):
        return ''.join(sorted(word.lower()))
    grouped_words = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_letters(word)
            grouped_words[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in grouped_words.values()))
    return anagram_pairs <= 30