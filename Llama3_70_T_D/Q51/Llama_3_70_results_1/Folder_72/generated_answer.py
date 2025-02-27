def if_contains_anagrams(lst):
    anagram_dict = {}
    pairs = 0
    for word in lst:
        word_lower = ''.join(sorted(word.lower()))
        if word_lower in anagram_dict:
            anagram_dict[word_lower] += 1
        else:
            anagram_dict[word_lower] = 1
    for count in anagram_dict.values():
        pairs += count * (count - 1) // 2
    return pairs <= 188