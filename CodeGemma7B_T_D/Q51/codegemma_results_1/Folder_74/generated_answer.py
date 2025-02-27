def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 57