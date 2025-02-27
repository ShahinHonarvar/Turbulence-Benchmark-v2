def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(lower_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word].append(lower_word)
        else:
            anagrams[sorted_word] = [lower_word]
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count >= 25