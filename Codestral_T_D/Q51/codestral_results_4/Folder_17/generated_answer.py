from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = {}
    for word in lst:
        lowercase_word = word.lower()
        if len(lowercase_word) >= 3:
            sorted_word = ''.join(sorted(lowercase_word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count <= 22