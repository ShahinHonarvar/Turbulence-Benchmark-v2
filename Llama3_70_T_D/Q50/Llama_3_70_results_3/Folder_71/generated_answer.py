def if_contains_anagrams(list_of_strings):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i]
            str2 = list_of_strings[j]
            if len(str1) >= 3 and len(str2) >= 3 and are_anagrams(str1, str2):
                anagram_pairs += 1
            if anagram_pairs >= 57:
                return True
    return False