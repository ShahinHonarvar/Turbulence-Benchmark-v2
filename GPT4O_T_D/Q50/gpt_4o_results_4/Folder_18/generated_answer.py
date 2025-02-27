from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = []
    for word in words:
        if len(word) >= 3:
            word_count = Counter(word.lower())
            anagram_counts.append(word_count)
    anagram_pairs = 0
    for i in range(len(anagram_counts)):
        for j in range(i + 1, len(anagram_counts)):
            if anagram_counts[i] == anagram_counts[j]:
                anagram_pairs += 1
                if anagram_pairs >= 106:
                    return True
    return False