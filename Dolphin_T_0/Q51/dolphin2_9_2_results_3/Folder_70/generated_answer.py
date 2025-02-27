from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            counter_word = Counter(word.lower())
            for other_word in lst:
                if len(other_word) >= 3 and other_word != word:
                    counter_other_word = Counter(other_word.lower())
                    if counter_word == counter_other_word:
                        count += 1
                        break
            if count > 97:
                return True
    return False