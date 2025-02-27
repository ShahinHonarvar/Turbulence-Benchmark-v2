def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            a = sorted(strings[i].lower())
            b = sorted(strings[j].lower())
            if a == b and len(strings[i]) >= 3:
                count += 1
    return count <= 474