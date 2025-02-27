def if_contains_anagrams(lst):
    anagrams_dict = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word_lower)
        else:
            anagrams_dict[sorted_word] = [word_lower]
    count = 0
    for value in anagrams_dict.values():
        if len(value) > 1 and len(value[0]) >= 3:
            count += len(value) * (len(value) - 1) // 2
    return count >= 194