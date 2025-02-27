def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values() if count > 1))
    return anagram_pairs >= 26