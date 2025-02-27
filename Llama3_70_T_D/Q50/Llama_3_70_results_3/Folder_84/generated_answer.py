def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        if len(word) >= 3:
            word_lower = word.lower()
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word_lower)
            else:
                anagrams[sorted_word] = [word_lower]
    for item in anagrams.values():
        count += len(item) * (len(item) - 1) // 2
    return count >= 108