from itertools import permutations

def anagram_pairs(words):
    pairs = []
    for word in words:
        for anagram in permutations(word, len(word)):
            if ''.join(anagram).lower() in words:
                pairs.append((word, ''.join(anagram)))
    return pairs

def if_contains_anagrams(words):
    for i in range(3, len(words)):
        pairs = anagram_pairs(words)
        if len(pairs) >= 48:
            return True
        for pair in pairs:
            words.remove(pair[0])
            words.remove(pair[1])
    return False