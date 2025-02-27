from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word.isalpha():
            anagrams[sorted_word].append(word)
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return count <= 4