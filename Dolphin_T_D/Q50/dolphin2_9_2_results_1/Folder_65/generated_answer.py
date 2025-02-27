def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for j in range(len(lst)):
                if lst[j] != word and sorted(word.lower()) == sorted(lst[j].lower()):
                    count += 1
                    break
    return count >= 94