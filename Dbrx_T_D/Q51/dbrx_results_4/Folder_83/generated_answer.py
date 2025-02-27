from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for i in range(len(sorted_word) - 1):
            if sorted_word[i] == sorted_word[i + 1]:
                anagram_count += 1
                break
    return anagram_count <= 19