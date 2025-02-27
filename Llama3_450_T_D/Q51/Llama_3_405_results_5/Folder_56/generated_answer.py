from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word.isalpha():
            anagrams[sorted_word].append(word)
    count = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values() if len(words) > 1))
    return count <= 11