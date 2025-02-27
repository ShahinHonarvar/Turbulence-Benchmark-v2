from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1.lower() != word2.lower() and (Counter(word1.lower()) == Counter(word2.lower())):
                    count += 1
                    if count >= 50:
                        return True
    return False