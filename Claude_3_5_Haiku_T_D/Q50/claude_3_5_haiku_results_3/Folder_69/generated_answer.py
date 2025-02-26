def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_count += 1
    return anagram_count >= 188