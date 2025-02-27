from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            word_sorted = ''.join(sorted(word))
            seen.add(word_sorted)
            if word_sorted in seen:
                count += 1
                seen.remove(word_sorted)
            if count == 401:
                return True
    return False