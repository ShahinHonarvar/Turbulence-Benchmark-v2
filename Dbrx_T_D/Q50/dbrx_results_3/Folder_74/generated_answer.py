def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 17]
    return len(anagram_pairs) > 0