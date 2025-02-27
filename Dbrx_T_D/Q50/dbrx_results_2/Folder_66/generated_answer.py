import string

def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    total_anagrams = sum((len(words) for words in anagrams.values() if len(words) >= 2))
    return total_anagrams >= 92