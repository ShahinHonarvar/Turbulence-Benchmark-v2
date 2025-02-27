def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            word_sorted = ''.join(sorted(word))
            if word_sorted not in anagrams:
                anagrams[word_sorted] = [word]
            else:
                anagrams[word_sorted].append(word)
    return len([pair for pair in anagrams.values() if len(pair) >= 2]) >= 64