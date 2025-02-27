def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    for value in anagrams.values():
        if len(value) > 1 and len(value[0]) >= 3:
            count += len(value) * (len(value) - 1) // 2
    return count >= 277