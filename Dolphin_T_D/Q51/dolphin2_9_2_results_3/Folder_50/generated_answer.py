def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    pairs = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            pairs += len(value) * (len(value) - 1) // 2
    return pairs <= 47