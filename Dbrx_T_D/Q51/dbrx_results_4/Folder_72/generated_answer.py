from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    count = 0
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
        if len(anagrams[sorted_word]) == 2 and len(word) >= 3:
            count += 1
    return count <= 188