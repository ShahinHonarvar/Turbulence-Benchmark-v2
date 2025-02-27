def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = ''.join(filter(str.isalpha, word)).lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    pairs = 0
    for words in anagrams.values():
        pairs += len(words) * (len(words) - 1) // 2
    return pairs <= 423