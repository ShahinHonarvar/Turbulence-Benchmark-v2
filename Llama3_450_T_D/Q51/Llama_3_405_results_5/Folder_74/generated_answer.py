def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower = ''.join(filter(str.isalpha, word)).lower()
        sorted_word = ''.join(sorted(lower))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for words in anagrams.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
    return count <= 57