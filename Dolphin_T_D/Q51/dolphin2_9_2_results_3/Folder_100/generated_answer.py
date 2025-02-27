def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                sorted_str1 = sorted(strings[i].lower())
                sorted_str2 = sorted(strings[j].lower())
                if sorted_str1 == sorted_str2:
                    anagram_pairs += 1
                if anagram_pairs >= 98:
                    return True
    return False