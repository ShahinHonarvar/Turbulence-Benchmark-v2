def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    for value in anagrams.values():
        count += value - 1
    return count <= 3