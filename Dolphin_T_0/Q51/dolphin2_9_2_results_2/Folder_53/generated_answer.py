def if_contains_anagrams(lst):
    count = 0
    d = {}
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word in d:
                count += 1
                d[word] += 1
            else:
                d[word] = 1
    return count <= 8