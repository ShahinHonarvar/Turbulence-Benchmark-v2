def if_contains_anagrams(list_of_strings):

    def is_anagram(str1, str2):
        if len(str1) != len(str2) or len(str1) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
                if count > 173:
                    return False
    return True