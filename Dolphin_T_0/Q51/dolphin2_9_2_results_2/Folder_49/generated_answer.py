def if_contains_anagrams(words):
    word_set = set()
    anagram_pairs = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_set:
                anagram_pairs += 1
                if anagram_pairs > 10:
                    return False
            else:
                word_set.add(sorted_word)
    return True