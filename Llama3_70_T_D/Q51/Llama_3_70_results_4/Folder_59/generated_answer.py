def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    for key, value in anagrams.items():
        if len(key) >= 3 and len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count <= 15