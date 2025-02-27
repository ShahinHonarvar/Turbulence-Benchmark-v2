def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1, s2 = (strings[i].lower(), strings[j].lower())
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                count += 1
    return count >= 78