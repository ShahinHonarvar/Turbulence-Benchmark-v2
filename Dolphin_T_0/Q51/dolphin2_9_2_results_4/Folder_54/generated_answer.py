def if_contains_anagrams(list_of_strings):
    anagram_pairs = set()
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) < 3 or len(str2) < 3:
                continue
            if sorted(str1) == sorted(str2):
                anagram_pairs.add((i, j))
                anagram_pairs.add((j, i))
    return len(anagram_pairs) <= 39