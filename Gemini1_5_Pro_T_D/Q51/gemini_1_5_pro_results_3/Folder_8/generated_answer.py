from collections import Counter

def if_contains_anagrams(list_of_strings):

    def are_anagrams(str1, str2):
        return len(str1) >= 3 and len(str2) >= 3 and (Counter(str1.lower()) == Counter(str2.lower()))
    count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if are_anagrams(list_of_strings[i], list_of_strings[j]):
                count += 1
                if count > 68:
                    return False
    return True