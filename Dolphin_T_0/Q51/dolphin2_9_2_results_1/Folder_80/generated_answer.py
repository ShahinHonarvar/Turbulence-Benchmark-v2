def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return pairs <= 255