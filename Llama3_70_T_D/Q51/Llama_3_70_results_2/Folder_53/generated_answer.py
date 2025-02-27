def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        word_sorted = ''.join(sorted(filter(str.isalpha, word_lower)))
        if len(word_sorted) < 3:
            continue
        if word_sorted in anagrams:
            anagrams[word_sorted] += 1
        else:
            anagrams[word_sorted] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 8