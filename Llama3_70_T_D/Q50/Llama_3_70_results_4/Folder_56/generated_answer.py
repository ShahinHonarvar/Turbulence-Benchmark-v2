def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagrams and len(lower_word) >= 3:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    for key in anagrams:
        if anagrams[key] >= 2 and len(key) >= 3:
            count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 77