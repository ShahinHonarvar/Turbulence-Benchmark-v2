import collections
import string

def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            word1_low = word1.lower()
            for word2 in lst:
                if len(word2) >= 3:
                    word2_low = word2.lower()
                    if collections.Counter(word1_low) == collections.Counter(word2_low) and word1_low != word2_low:
                        count += 1
                        if count >= 61:
                            return False
    return count <= 61