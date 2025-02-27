from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            for other_word in lst:
                if len(other_word) >= 3 and other_word != word:
                    if Counter(other_word.lower()) == c:
                        count += 1
    return count >= 36