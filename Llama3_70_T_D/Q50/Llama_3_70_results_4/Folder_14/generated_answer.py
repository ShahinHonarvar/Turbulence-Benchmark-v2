def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = sorted(strings[i].lower())
            s2 = sorted(strings[j].lower())
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (s1 == s2):
                anagrams_count += 1
    return anagrams_count >= 22