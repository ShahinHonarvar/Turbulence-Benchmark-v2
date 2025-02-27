def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word_lower)
        else:
            anagram_dict[sorted_word] = [word_lower]
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            count += 1
    return count >= 2