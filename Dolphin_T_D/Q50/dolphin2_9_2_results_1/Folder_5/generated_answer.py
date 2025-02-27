def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        word = word.lower()
        if len(word) >= 3 and sorted(word) in seen:
            count += 1
            if count >= 21:
                return True
        seen.add(sorted(word))
    return False