def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_set:
            anagram_count += 1
        else:
            anagram_set.add(sorted_word)
    return anagram_count >= 9