import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = set()
            anagrams[sorted_word].add(word)
    total_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values()))
    return total_pairs >= 49