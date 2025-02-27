import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        elif len(sorted_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word].append(word)
    anagram_pairs = sum((len(value) // 2 for value in anagrams.values()))
    return anagram_pairs <= 98