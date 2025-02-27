def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count <= 401