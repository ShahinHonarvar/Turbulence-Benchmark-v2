def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = ''.join(filter(str.isalpha, word)).lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    pairs = sum((n * (n - 1) for n in anagrams.values()))
    return pairs <= 93