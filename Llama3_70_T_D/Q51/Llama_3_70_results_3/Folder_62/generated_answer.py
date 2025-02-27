def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted((c for c in word.lower() if c.isalpha())))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 289