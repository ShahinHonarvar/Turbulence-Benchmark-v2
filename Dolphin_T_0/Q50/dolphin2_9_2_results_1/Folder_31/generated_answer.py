def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            anagrams = [''.join(sorted(word.lower()))]
            for another_word in lst:
                if len(another_word) >= 3 and another_word != word and (''.join(sorted(another_word.lower())) in anagrams):
                    anagrams.append(''.join(sorted(another_word.lower())))
            count += len(anagrams) - 1
            if count >= 68:
                return True
    return False