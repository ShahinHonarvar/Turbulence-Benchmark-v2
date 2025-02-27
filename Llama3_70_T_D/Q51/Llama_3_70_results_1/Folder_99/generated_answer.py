def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word_lower) >= 3 and sorted_word in anagrams:
            count += 1
        anagrams[sorted_word] = True
    return count <= 93