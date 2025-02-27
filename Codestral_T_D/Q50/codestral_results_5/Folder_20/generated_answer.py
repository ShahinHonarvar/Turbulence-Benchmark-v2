def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return any((len(val) >= 2 for val in anagrams.values())) and sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values())) >= 64