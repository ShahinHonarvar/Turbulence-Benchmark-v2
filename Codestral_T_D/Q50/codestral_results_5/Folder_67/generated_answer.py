def if_contains_anagrams(lst):
    counter = 0
    dictionary = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in dictionary:
                counter += dictionary[sorted_word]
                dictionary[sorted_word] += 1
            else:
                dictionary[sorted_word] = 1
    return counter >= 41