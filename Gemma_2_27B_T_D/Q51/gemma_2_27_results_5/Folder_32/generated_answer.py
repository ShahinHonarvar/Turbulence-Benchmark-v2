from collections import Counter

def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i].lower()
            word2 = words[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
                count += 1
    return count <= 89