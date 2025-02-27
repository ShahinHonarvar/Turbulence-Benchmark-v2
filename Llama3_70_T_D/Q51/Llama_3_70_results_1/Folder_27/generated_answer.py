def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1 = ''.join(filter(str.isalpha, strings[i].lower()))
            s2 = ''.join(filter(str.isalpha, strings[j].lower()))
            if len(s1) < 3 or len(s2) < 3:
                continue
            if sorted(s1) == sorted(s2):
                anagrams_count += 1
    return anagrams_count <= 113