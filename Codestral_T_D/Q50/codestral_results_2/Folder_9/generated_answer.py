def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            anagram_pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_pairs >= 66