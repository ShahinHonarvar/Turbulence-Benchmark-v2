def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 411