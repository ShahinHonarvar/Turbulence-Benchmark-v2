def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count >= 59