def if_contains_anagrams(words):
    anagrams = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            w1 = words[i].lower()
            w2 = words[j].lower()
            if len(w1) >= 3 and len(w2) >= 3:
                if sorted(w1) == sorted(w2):
                    anagrams += 1
    return anagrams <= 25