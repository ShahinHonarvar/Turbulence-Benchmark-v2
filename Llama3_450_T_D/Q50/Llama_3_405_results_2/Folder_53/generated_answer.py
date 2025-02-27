def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 11