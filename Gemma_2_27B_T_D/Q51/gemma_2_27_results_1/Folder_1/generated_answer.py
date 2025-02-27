def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if i != j and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                a = sorted(strings[i].lower())
                b = sorted(strings[j].lower())
                if a == b:
                    count += 1
    return count <= 30