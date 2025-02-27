def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            string1 = strings[i].lower()
            string2 = strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                if sorted(string1) == sorted(string2) and string1 != string2:
                    count += 1
    return count <= 210