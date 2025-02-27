from itertools import permutations

def if_contains_anagrams(input_list):
    anagrams = []
    for word_1 in input_list:
        for word_2 in input_list:
            if word_1 != word_2 and sorted(word_1.lower()) == sorted(word_2.lower()):
                if len(word_1.lower()) >= 3 and len(word_2.lower()) >= 3:
                    anagrams.append((word_1, word_2))
    if len(anagrams) >= 18:
        return True
    else:
        return False