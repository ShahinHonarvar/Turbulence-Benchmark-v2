def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    pairs = 0
    for anagram in anagrams.values():
        if len(anagram) > 1:
            pairs += len(anagram) * (len(anagram) - 1) // 2
    return pairs >= 54