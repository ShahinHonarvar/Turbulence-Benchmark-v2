def if_contains_anagrams(list_of_strings):
    equiv_dict = {}
    length_should_be = 3
    min_pairs = 40
    for word in list_of_strings:
        if len(word) >= length_should_be:
            word_lower = word.lower()
            equiv_class = ''.join(sorted(word_lower))
            if equiv_class in equiv_dict:
                equiv_dict[equiv_class] += 1
            else:
                equiv_dict[equiv_class] = 1
    count = sum((1 for v in equiv_dict.values() if v > 1))
    return count >= min_pairs