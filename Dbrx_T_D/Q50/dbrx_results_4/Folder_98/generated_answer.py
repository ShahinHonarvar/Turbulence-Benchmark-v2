def if_contains_anagrams(words):
    if len(words) < 14:
        return False
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return len([v for v in anagrams.values() if len(v) > 1]) >= 7