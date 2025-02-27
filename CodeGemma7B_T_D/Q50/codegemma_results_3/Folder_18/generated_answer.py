def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    count = 0
    for value in anagrams.values():
        if value >= 2:
            count += value * (value - 1) // 2
    return count >= 106