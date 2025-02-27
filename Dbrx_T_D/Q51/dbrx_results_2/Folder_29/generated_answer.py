import string

def if_contains_anagrams(lst):
    anagrams = set()
    count = 0
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            anagrams.add(sorted_word)
    for anagram in anagrams:
        count += len([word for word in lst if ''.join(sorted(word.lower())) == anagram]) - 1
    return count <= 318