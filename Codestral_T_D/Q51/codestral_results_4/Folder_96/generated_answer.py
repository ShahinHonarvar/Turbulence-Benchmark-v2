def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(lower_word)
            else:
                anagrams[sorted_word] = [lower_word]
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            anagram_count += 1
    return anagram_count <= 2