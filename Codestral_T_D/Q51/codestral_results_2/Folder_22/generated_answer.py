def if_contains_anagrams(strings):
    anagram_pairs = 0
    words = {}
    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words:
                anagram_pairs += 1
            else:
                words[sorted_word] = 1
    return anagram_pairs <= 14