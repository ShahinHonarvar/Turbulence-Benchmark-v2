def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                count += 1
            elif anagrams.get(sorted_word, 0) == 1:
                anagrams[sorted_word] = 2
                count += 1
            else:
                anagrams[sorted_word] = 1
    return count <= 36