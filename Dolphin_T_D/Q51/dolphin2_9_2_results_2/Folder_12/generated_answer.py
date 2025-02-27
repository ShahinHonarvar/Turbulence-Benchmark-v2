def if_contains_anagrams(lst):
    count = 0
    s = set()
    for word in lst:
        for w in s:
            if sorted(w.lower()) == sorted(word.lower()):
                count += 1
                break
        s.add(word)
    return count <= 92