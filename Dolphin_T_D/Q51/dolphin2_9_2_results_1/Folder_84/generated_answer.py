from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagrams:
                if anagrams[sorted_word] < 1 or anagrams[sorted_word] == word_lower:
                    anagrams[sorted_word] = word_lower
                    count += 1
            else:
                anagrams[sorted_word] = word_lower
    return count <= 16