from collections import Counter

def if_contains_anagrams(words):
    anagrams = 0
    words = [word.lower() for word in words if len(word) >= 3]
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if Counter(words[i]) == Counter(words[j]):
                anagrams += 1
                if anagrams > 21:
                    return False
    return True