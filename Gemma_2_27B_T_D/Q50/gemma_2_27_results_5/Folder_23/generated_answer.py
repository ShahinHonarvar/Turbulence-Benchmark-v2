def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = sorted(strings[i].lower())
            str2 = sorted(strings[j].lower())
            if str1 == str2 and len(str1) >= 3:
                count += 1
    return count >= 67