def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            count += 1
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return pairs <= 276