def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    for v in anagrams.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count >= 68