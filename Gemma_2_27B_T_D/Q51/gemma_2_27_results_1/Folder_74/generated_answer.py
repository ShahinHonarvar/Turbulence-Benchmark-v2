def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            a = ''.join(sorted(strings[i].lower()))
            b = ''.join(sorted(strings[j].lower()))
            if len(a) >= 3 and a == b:
                count += 1
    return count <= 57