def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = 0
        anagrams[sorted_word] += 1
    return sum((v for v in anagrams.values() if v >= 18)) >= 18