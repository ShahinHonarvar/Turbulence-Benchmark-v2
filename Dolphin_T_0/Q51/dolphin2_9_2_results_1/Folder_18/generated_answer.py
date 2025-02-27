from collections import Counter

def if_contains_anagrams(arr):
    anagrams = 0
    for i in range(len(arr)):
        if len(arr[i]) >= 3:
            for j in range(i + 1, len(arr)):
                if len(arr[j]) >= 3:
                    if Counter(arr[i].lower()) == Counter(arr[j].lower()):
                        anagrams += 1
    return anagrams <= 42