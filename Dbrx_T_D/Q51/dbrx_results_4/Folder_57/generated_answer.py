from collections import defaultdict

def if_contains_anagrams(words: List[str]) -> bool:
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        anagrams[sorted_word].append(word_lower)
    pairs_of_anagrams = sum((len(values) // 2 for values in anagrams.values()))
    return pairs_of_anagrams <= 74