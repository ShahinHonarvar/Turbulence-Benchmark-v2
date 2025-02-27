from collections import Counter

def if_contains_anagrams(list_strings):
    result = False
    counter = Counter()
    for word in list_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in counter:
                counter[sorted_word] += 1
                if counter[sorted_word] > 1:
                    result = True
            else:
                counter[sorted_word] = 1
    return result