def if_contains_anagrams(lst):
    counter = 0
    for word in lst:
        if len(word) > 2:
            for second_word in lst:
                if sorted(word.lower()) == sorted(second_word.lower()):
                    counter += 1
    return counter >= 69