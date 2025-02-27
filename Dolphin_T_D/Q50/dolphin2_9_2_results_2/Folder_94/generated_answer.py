def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for other_word in lst:
                if len(other_word) >= 3 and sorted(word.lower()) == sorted(other_word.lower()) and (word != other_word):
                    count += 1
                    break
    return count >= 46