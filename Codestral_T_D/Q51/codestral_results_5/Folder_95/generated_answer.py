def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [lower_word]
            else:
                anagrams[sorted_word].append(lower_word)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return anagram_pairs <= 6