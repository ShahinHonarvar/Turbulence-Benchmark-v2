from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    seen = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                count += seen[sorted_word]
                seen[sorted_word] += 1
            else:
                seen[sorted_word] = 1
    return count >= 14