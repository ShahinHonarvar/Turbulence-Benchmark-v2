from collections import Counter

def if_contains_anagrams(wordList):
    counter = Counter()
    for word in wordList:
        if len(word) >= 3:
            sortedWord = ''.join(sorted(word.lower()))
            counter[sortedWord] += 1
    count = 0
    for c in counter.values():
        count += c * (c - 1) // 2
    return count <= 206