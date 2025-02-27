import collections

def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_count = 0
    for i in range(len(anagrams)):
        if anagrams.count(anagrams[i]) > 1:
            anagram_count += 1
    return anagram_count <= 84