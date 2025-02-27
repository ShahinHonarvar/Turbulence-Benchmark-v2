def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word_lower)
        else:
            anagrams[sorted_word] = [word_lower]
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(key) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 39