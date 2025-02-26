def if_contains_anagrams(strings):
    anagram_count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    anagram_count += 1
    return anagram_count >= 61