def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = sorted(strings[i].lower())
            s2 = sorted(strings[j].lower())
            if s1 == s2 and len(strings[i]) >= 3:
                count += 1
    return count <= 181