import collections

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i]
            str2 = list_of_strings[j]
            if len(str1) >= 3 and len(str2) >= 3 and (str1.lower() != str2.lower):
                if collections.Counter(str1.lower()) == collections.Counter(str2.lower()):
                    anagram_count += 1
                    if anagram_count >= 64:
                        return True
    return False