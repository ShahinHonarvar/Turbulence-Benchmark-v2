def if_contains_anagrams(lst):
    counter = 0
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                counter += anagrams[sorted_word]
                anagrams[sorted_word] += 1
    return counter >= 143