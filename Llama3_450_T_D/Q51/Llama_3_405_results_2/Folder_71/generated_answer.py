def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        word_lower = ''.join(sorted(word.lower()))
        if word_lower in anagram_dict:
            anagram_dict[word_lower] += 1
        else:
            anagram_dict[word_lower] = 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs <= 9