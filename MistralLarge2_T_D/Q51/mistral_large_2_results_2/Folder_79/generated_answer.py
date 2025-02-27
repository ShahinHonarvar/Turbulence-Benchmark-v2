from collections import defaultdict

def if_contains_anagrams(words):
    sorted_words = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            sorted_words[sorted_word].append(word)
    anagram_pairs = [len(words) for words in sorted_words.values() if len(words) > 1]
    total_pairs = sum((len(words) * (len(words) - 1) // 2 for words in sorted_words.values() if len(words) > 1))
    return total_pairs <= 173