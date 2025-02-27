from collections import defaultdict

def if_contains_anagrams(words):
    """Returns True if there are at most 89 pairs of anagrams in the given list."""
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    return len(anagrams) <= 89