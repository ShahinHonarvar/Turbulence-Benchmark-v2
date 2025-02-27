def if_contains_anagrams(lst):
    anagrams_count = {}
    for word in lst:
        word_lower = ''.join(filter(str.isalpha, word)).lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams_count:
            anagrams_count[sorted_word] += 1
        else:
            anagrams_count[sorted_word] = 1
    pairs_count = sum((value * (value - 1) // 2 for value in anagrams_count.values()))
    return pairs_count <= 85