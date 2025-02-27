def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = ''.join(sorted(strings[i].lower()[len(strings[i]) >= 3:].strip()))
            str2 = ''.join(sorted(strings[j].lower()[len(strings[j]) >= 3:].strip()))
            if str1 == str2 and i != j:
                count += 1
    return count <= 77