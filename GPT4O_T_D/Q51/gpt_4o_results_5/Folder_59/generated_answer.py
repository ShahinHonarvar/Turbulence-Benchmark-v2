def if_contains_anagrams(words):

    def sorted_characters(s):
        return ''.join(sorted(s.lower()))
    candidates = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_characters(word)
            if sorted_word in candidates:
                candidates[sorted_word] += 1
            else:
                candidates[sorted_word] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in candidates.values() if count >= 2))
    return anagram_pairs <= 15