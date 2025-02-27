def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagrams.values())) <= 41