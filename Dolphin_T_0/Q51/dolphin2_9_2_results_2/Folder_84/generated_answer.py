def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                count += 1
                anagrams[sorted_word] += 1
    return count <= 16