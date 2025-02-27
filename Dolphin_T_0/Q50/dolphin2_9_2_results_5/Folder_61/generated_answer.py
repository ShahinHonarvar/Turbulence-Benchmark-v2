def if_contains_anagrams(lst):
    counter = 0
    for word in lst:
        j = 0
        if len(word) >= 3:
            while j < len(lst):
                if lst[j] != word and sorted(word.lower()) == sorted(lst[j].lower()):
                    counter += 1
                    if counter >= 8:
                        return True
                j += 1
    return False