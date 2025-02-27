from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    counter = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            counter += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return counter >= 47