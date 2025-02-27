import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    anagram_pairs = sum([len(list(v)) // 2 for k, v in itertools.groupby(sorted(anagrams.values()))])
    return anagram_pairs >= 108