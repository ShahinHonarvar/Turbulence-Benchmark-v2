def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) < 3 or not word_lower.isalpha():
            continue
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    count = sum([v * (v - 1) // 2 for v in anagrams.values()])
    return count <= 116