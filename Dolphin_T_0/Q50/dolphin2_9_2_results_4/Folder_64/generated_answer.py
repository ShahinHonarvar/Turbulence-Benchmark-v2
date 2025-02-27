def if_contains_anagrams(lst):
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            for second_word in lst:
                if len(second_word) >= 3:
                    if sort_word(word) == sort_word(second_word):
                        pairs += 1
    if pairs >= 5:
        return True
    else:
        return False

def sort_word(word):
    return ''.join(sorted(word.lower()))