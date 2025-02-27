def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                str1 = sorted(strings[i].lower())
                str2 = sorted(strings[j].lower())
                if str1 == str2:
                    count += 1
    return count <= 5