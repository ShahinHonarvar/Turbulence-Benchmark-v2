def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            s = ''.join(sorted(word.lower()))
            if s in seen:
                count += 1
            else:
                seen.add(s)
    return count >= 4