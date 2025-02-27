def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return anagram_pairs <= 50