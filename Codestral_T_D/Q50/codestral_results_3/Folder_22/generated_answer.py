def if_contains_anagrams(lst):
    anagram_pairs = set()
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagram_pairs:
            return True
        anagram_pairs.add(sorted_word)
    return False