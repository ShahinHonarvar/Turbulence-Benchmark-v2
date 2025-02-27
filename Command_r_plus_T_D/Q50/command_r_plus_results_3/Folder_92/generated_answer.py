def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = [pair for pair in anagram_dict.values() if len(pair) >= 2]
    anagram_pairs_count = len(anagram_pairs)
    return anagram_pairs_count >= 2