def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(lower_word)
        else:
            anagrams[sorted_word] = [lower_word]
    for anagram in anagrams.values():
        count += len(anagram) * (len(anagram) - 1) // 2
    return count >= 21