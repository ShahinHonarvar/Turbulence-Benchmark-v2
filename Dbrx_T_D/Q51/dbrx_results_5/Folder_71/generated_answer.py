import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    english_letters = re.findall('[a-zA-Z]{3,}', ' '.join(words))
    for word in english_letters:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    return sum((len(v) <= 9 for v in anagrams.values())) == len(anagrams)