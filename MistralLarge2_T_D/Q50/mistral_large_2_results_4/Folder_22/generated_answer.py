from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values() if len(group) > 1))
    return count >= 72