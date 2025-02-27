import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    anagram_count = sum((1 for value in anagrams.values() if len(value) >= 2))
    return anagram_count >= 3