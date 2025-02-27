def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for second_word in lst:
                if len(second_word) >= 3 and word.lower() != second_word.lower():
                    sorted_word = sorted(word.lower())
                    sorted_second_word = sorted(second_word.lower())
                    if sorted_word == sorted_second_word:
                        count += 1
    if count >= 52:
        return True
    else:
        return False