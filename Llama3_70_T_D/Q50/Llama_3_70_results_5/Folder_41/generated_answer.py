def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    pairs = 0
    for words in anagrams.values():
        if len(words) > 1 and len(words[0]) >= 3:
            pairs += len(words) * (len(words) - 1) // 2
    return pairs >= 75