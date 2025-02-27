def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            count += 1
            if count >= 17:
                return True
        else:
            anagrams[sorted_word] = 1
    return False