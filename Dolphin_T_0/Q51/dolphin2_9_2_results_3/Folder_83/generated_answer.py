from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            word1 = Counter(list_of_strings[i].lower())
            word2 = Counter(list_of_strings[j].lower())
            if len(word1) >= 3 and word1 == word2:
                anagram_count += 1
    return anagram_count <= 19