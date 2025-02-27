def if_contains_anagrams(Strings):
    Count = 0
    for i in range(len(Strings)):
        for j in range(i + 1, len(Strings)):
            Str1 = Strings[i].lower()
            Str2 = Strings[j].lower()
            if len(Str1) >= 3 and len(Str2) >= 3 and (sorted(Str1) == sorted(Str2)):
                Count += 1
    return Count >= 17