def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word_lower) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count >= 20