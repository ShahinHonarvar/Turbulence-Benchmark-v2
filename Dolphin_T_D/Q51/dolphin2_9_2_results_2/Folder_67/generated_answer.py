def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                s1 = sorted(strings[i].lower())
                s2 = sorted(strings[j].lower())
                if s1 == s2:
                    count += 1
        if count > 5:
            return False
    return count <= 5