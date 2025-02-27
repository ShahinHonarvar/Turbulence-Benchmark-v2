def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
        else:
            continue
        if sorted_word in anagrams:
            if anagrams[sorted_word][1] == False:
                count += 1
                if count > 113:
                    return False
                else:
                    anagrams[sorted_word][1] = True
            else:
                anagrams[sorted_word][0] += 1
        else:
            anagrams[sorted_word] = [1, False]
    return True