def if_contains_anagrams(lst):
    pair_counter = 0
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            pair_counter += 1
            if pair_counter >= 177:
                return True
    return False