import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_letters for c in sorted_word)):
            anagrams.append(sorted_word)
    anagram_pairs = len(set(anagrams)) - len(anagrams)
    return anagram_pairs <= 84