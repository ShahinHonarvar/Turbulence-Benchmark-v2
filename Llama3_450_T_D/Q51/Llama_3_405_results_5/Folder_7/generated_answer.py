def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            count += anagrams[sorted_word]
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return count <= 445