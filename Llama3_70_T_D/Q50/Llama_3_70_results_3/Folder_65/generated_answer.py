def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) > 2:
            word_sorted = ''.join(sorted(word_lower))
            if word_sorted in anagram_dict:
                anagram_dict[word_sorted] += 1
            else:
                anagram_dict[word_sorted] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 94