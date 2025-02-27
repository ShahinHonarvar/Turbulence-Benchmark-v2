def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        sorted_str1 = ''.join(sorted(lst[i].lower()))
        for j in range(i + 1, len(lst)):
            sorted_str2 = ''.join(sorted(lst[j].lower()))
            if sorted_str1 == sorted_str2 and len(lst[i]) >= 3:
                anagram_count += 1
    return anagram_count >= 69