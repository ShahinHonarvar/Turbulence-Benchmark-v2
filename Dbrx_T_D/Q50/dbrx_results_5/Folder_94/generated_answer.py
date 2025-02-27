import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_char = ''.join(sorted(word.lower()))
        if len(sorted_char) >= 3:
            anagrams.append(sorted_char)
    anagram_set = set()
    for anagram in anagrams:
        if anagram in anagram_set:
            return True
        anagram_set.add(anagram)
    return False