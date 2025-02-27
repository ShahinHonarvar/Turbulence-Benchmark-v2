import re
from collections import Counter

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        word = re.sub('[^a-zA-Z]', '', word).lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams.append(sorted_word)
    anagram_counts = Counter(anagrams)
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 131