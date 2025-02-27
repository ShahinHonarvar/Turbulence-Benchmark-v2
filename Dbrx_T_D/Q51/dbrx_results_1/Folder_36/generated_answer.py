from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(set)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word].add(word)
        if len(anagrams[sorted_word]) > 1:
            return True
    return len(anagrams) > 25