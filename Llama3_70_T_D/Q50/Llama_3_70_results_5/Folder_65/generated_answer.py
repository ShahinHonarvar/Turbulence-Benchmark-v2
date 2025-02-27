def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagrams = {}
    pairs = 0
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for words in anagrams.values():
        pairs += len(words) * (len(words) - 1) // 2
    return pairs >= 94