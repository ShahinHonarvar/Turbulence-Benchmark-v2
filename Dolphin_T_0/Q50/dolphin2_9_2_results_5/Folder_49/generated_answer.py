def if_contains_anagrams(lst):
    anagrams = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagrams.append((lst[i], lst[j]))
    if len(anagrams) >= 59:
        return True
    else:
        return False