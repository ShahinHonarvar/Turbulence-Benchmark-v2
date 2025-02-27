from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    string_set = set(strings)
    for word in string_set:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for other_word in string_set:
                if other_word != word and len(other_word) >= 3 and (word.lower() != other_word.lower()):
                    other_sorted_word = ''.join(sorted(other_word.lower()))
                    if sorted_word == other_sorted_word:
                        count += 1
    return count <= 48