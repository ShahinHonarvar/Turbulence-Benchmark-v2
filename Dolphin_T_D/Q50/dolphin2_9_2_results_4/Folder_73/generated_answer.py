def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) > 2:
            s = ''.join(sorted(word.lower()))
            try:
                anagrams[s] += 1
            except KeyError:
                anagrams[s] = 1
                if anagrams[s] > 1:
                    count += 1
    if count >= 91:
        return True
    else:
        return False