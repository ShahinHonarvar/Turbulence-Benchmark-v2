def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) > 1 and len(pair[0]) >= 3]
    return len(anagram_pairs) >= 2