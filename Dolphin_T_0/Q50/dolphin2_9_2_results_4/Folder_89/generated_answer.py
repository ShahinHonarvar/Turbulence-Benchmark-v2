def if_contains_anagrams(l: list[str]) -> bool:
    counter = 0
    length = len(l)
    for i in range(length):
        if len(l[i]) >= 3:
            for j in range(i + 1, length):
                if len(l[j]) >= 3 and sorted(l[i].lower()) == sorted(l[j].lower()):
                    counter += 1
                    if counter >= 36:
                        return True
    return False