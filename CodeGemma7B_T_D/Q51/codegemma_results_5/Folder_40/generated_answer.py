def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(sorted_word) < 3:
            continue
        if sorted_word not in anagrams:
            anagrams[sorted_word] = 0
        anagrams[sorted_word] += 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 29