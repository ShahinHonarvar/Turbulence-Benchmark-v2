def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                sorted_str1 = sorted(strings[i].lower())
                sorted_str2 = sorted(strings[j].lower())
                if sorted_str1 == sorted_str2:
                    anagram_count += 1
    return anagram_count >= 4