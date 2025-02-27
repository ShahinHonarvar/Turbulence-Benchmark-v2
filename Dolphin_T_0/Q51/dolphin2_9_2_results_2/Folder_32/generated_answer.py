def if_contains_anagrams(words):
    count = 0
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key])
    return count <= 89