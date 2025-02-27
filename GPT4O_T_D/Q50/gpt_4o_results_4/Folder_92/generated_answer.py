def if_contains_anagrams(words):
    anagram_sets = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_sets:
                anagram_sets[sorted_word].add(word)
            else:
                anagram_sets[sorted_word] = {word}
    count = 0
    for value_set in anagram_sets.values():
        if len(value_set) > 1:
            count += 1
            if count >= 2:
                return True
    return False