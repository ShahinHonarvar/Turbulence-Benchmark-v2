from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            counter = Counter(word.lower())
            for other_word in lst:
                if len(other_word) >= 3 and other_word != word and (Counter(other_word.lower()) == counter):
                    count += 1
                    if count == 50:
                        return True
    return count == 0 or count // 2 <= 49