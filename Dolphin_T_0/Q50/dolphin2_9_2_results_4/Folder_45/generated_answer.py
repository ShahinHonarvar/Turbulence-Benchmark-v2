def if_contains_anagrams(lst):
    count = 0
    for a in range(len(lst)):
        for b in range(a + 1, len(lst)):
            if len(lst[a]) >= 3 and len(lst[b]) >= 3:
                if sorted(lst[a].lower()) == sorted(lst[b].lower()):
                    count += 1
                    if count >= 277:
                        return True
    return False