import sys
from collections import defaultdict

def if_contains_anagrams(words):
    if sys.version_info[0] < 3:
        words = [word.lower() for word in words]
    else:
        words = [word.lower() for word in words if isinstance(word, str)]
    anagram_count = 0
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    for anagram in anagrams.values():
        if len(anagram) >= 3:
            anagram_count += len(anagram) * (len(anagram) - 1) // 2
    return anagram_count <= 423