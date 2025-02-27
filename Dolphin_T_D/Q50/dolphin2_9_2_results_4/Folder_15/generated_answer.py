def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key] += 1
                anagrams[key] %= 2
                if anagrams[key] == 0:
                    return True
            else:
                anagrams[key] = 1
    return False