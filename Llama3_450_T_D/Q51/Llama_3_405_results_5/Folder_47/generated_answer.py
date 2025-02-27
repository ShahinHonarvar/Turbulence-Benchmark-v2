def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word.isalpha():
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values() if n > 1))
    return count <= 366