from collections import Counter

def if_contains_anagrams(words):
    word_sets = [set(word.lower()) for word in words]
    anagram_sets = [set(Counter(word).most_common()) for word in words]
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if word_sets[i] == word_sets[j] and anagram_sets[i] == anagram_sets[j]:
                count += 1
    return count <= 116