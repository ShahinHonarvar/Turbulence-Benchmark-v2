from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    checked = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in checked:
                count += 1
            else:
                checked.add(sorted_word)
    return count <= 35