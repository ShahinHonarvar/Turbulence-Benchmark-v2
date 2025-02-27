import string

def if_contains_anagrams(strings):
    anagrams = []
    english_letters = string.ascii_lowercase
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((letter in english_letters for letter in sorted_word)):
            anagrams.append(sorted_word)
    anagram_pairs = [(anagrams.count(pair[0]), pair[0]) for pair in set((tuple(pair) for pair in anagrams))]
    anagram_freq = [pair[0] for pair in anagram_pairs]
    return sum(anagram_freq) <= 20