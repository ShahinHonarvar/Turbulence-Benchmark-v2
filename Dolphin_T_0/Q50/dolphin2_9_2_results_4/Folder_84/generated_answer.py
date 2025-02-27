def if_contains_anagrams(lst):
    result = False
    words_length_three = [word for word in lst if len(word) >= 3]
    for word_1 in words_length_three:
        word_1_lower = word_1.lower()
        for word_2 in words_length_three:
            word_2_lower = word_2.lower()
            if word_1_lower != word_2_lower and sorted(word_1_lower) == sorted(word_2_lower):
                words_length_three.remove(word_1)
                words_length_three.remove(word_2)
                result = True
    return result