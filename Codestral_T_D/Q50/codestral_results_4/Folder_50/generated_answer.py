from collections import defaultdict

def if_contains_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            groups[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in groups.values()))
    return anagram_pairs >= 20