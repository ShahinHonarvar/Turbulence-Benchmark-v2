def if_contains_anagrams(l):
    anagrams = {}
    for word in l:
        if len(word) < 3:
            continue
        word = ''.join(sorted(word.lower()))
        if word not in anagrams:
            anagrams[word] = [word]
        else:
            anagrams[word].append(word)
    return len(anagrams) > 35