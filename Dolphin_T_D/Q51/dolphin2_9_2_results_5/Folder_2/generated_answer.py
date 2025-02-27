def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                strings[i] = strings[i].lower()
                strings[j] = strings[j].lower()
                if sorted(strings[i]) == sorted(strings[j]):
                    anagram_count += 1
    return anagram_count <= 81