def if_contains_anagrams(lst):
    count = 0
    anagrams = dict()
    for word in lst:
        lowerword = word.lower()
        if len(lowerword) >= 3:
            sortedword = ''.join(sorted(lowerword))
            if sortedword in anagrams:
                count += 1
                anagrams[sortedword].append(lowerword)
            else:
                anagrams[sortedword] = [lowerword]
    return count >= 8