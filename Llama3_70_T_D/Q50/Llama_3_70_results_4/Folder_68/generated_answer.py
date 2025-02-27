def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    for key in anagrams:
        if anagrams[key] > 1:
            count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 9