def if_contains_anagrams(lst):
    anagram_pairs = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in seen:
                anagram_pairs += 1
            else:
                seen.add(sorted_word)
    return anagram_pairs <= 15