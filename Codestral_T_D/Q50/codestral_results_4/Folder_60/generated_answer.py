def if_contains_anagrams(strings):
    anagrams = {}
    for word in strings:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 60