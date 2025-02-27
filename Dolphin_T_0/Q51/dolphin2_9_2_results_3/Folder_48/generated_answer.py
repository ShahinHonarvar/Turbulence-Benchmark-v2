import collections

def if_contains_anagrams(words):
    count = 0
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3 and key not in anagrams and key.isalpha():
            count += 1
            anagrams[key] = True
    return count / 2 <= 277