def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            for w in seen:
                if sorted(w.lower()) == sorted(word.lower()):
                    count += 1
                    break
            seen.add(word.lower())
    return count <= 8