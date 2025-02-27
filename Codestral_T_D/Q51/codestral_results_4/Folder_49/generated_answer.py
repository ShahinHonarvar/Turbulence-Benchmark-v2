def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word.isalpha():
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    return sum((val * (val - 1) // 2 for val in anagrams.values())) <= 10