def if_contains_anagrams(lst):
    anagrams = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                key = ''.join(sorted(lst[i].lower()))
                if key not in anagrams:
                    anagrams[key] = [lst[i]]
                else:
                    anagrams[key].append(lst[i])
                if len(anagrams[key]) > 1:
                    if len(anagrams[key]) % 2 == 0:
                        return True
                    else:
                        return False
    return False