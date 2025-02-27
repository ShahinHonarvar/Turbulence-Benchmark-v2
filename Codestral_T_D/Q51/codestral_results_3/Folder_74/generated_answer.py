def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams))
    return anagram_pairs <= 57