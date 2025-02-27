from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = sum([len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams if len(anagrams[key]) >= 2])
    return count >= 59