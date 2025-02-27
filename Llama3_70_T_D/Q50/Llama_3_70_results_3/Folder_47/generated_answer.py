def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word_lower)
            else:
                anagrams[sorted_word] = [word_lower]
    for words in anagrams.values():
        count += len(words) * (len(words) - 1) // 2
    return count >= 47