import string

def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        sorted_words = [''.join(sorted(word.lower()))]
        if len(sorted_words) >= 3:
            anagrams.extend(sorted_words)
    anagram_pairs = sum((x.count(y) // 2 for x in anagrams for y in anagrams if x != y)) // 2
    return anagram_pairs <= 78