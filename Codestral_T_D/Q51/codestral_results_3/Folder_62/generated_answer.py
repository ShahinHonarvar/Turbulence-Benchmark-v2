def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return count <= 289