def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word = ''.join(filter(str.isalpha, word)).lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for words in anagrams.values():
        count += len(words) * (len(words) - 1) // 2
    return count <= 78