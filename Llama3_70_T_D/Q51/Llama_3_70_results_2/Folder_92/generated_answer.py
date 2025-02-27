def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = ''.join(filter(str.isalpha, lst[i].lower()))
            str2 = ''.join(filter(str.isalpha, lst[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_count += 1
    return anagram_count <= 34