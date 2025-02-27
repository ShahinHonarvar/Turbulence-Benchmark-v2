from collections import Counter

def if_contains_anagrams(lst):
    result = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in result:
                result[sorted_word] += 1
            else:
                result[sorted_word] = 1
    return max(result.values()) <= 22