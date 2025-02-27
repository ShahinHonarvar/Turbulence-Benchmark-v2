def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lowercase = word.lower()
        if len(word_lowercase) >= 3 and word_lowercase not in anagrams:
            sorted_word = ''.join(sorted(word_lowercase))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    pairs = sum((value // 2 for value in anagrams.values()))
    return pairs <= 25