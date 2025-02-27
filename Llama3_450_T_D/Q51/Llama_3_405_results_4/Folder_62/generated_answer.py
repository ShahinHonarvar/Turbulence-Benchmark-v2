from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    count = 0
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted([char.lower() for char in word if char.isalpha()]))
        count += anagrams[sorted_word]
        anagrams[sorted_word] += 1
    return count <= 289