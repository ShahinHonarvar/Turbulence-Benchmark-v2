import string

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((char in string.ascii_letters for char in sorted_word)):
            anagrams.append(sorted_word)
    anagram_pairs = [(a, b) for i, a in enumerate(anagrams) for b in anagrams[:i] if a != b and set(a) == set(b)]
    return len(anagram_pairs) <= 15