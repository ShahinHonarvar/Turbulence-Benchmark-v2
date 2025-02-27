def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    for count in anagrams.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 181