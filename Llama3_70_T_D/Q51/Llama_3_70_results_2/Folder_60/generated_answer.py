def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(lower_word)
        else:
            anagrams[sorted_word] = [lower_word]
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(key) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 77