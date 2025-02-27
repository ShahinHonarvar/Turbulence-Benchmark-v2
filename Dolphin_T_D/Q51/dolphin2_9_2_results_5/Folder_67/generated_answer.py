def if_contains_anagrams(lst):
    anagrams_found = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3:
                anagrams_found.append((lst[i], lst[j]))
                if len(anagrams_found) >= 5:
                    return True
    return False