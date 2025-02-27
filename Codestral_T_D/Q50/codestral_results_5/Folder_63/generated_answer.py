def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 89