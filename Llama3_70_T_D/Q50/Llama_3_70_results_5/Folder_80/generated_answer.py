def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        s1 = ''.join(sorted(strings[i].lower()))
        if len(s1) < 3:
            continue
        for j in range(i + 1, len(strings)):
            s2 = ''.join(sorted(strings[j].lower()))
            if len(s2) < 3:
                continue
            if s1 == s2 and strings[i].lower() != strings[j].lower():
                count += 1
                if count >= 19:
                    return True
    return False