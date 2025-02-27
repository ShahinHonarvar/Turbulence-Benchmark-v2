def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for value in anagrams.values():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
    return count >= 246