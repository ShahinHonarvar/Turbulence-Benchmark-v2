from collections import Counter

def if_contains_anagrams(words):
    anagrams = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if Counter(words[i].lower()) == Counter(words[j].lower()):
                    anagrams += 1
    return anagrams <= 91