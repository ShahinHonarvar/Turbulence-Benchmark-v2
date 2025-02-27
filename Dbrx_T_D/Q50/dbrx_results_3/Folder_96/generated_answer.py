import itertools

def if_contains_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = 0
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            anagram_pairs += len(anagram) * (len(anagram) - 1) // 2
            if anagram_pairs >= 98:
                return True
    return False