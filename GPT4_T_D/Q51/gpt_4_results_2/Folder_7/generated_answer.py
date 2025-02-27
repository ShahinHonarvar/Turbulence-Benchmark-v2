from collections import defaultdict

def if_contains_anagrams(lst):
    anagram = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram[sorted_word].append(word)
    pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram.values() if len(words) > 1))
    return pairs <= 445