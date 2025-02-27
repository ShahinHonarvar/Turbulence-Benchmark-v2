from collections import Counter

def if_contains_anagrams(list_of_strings):

    def is_anagram(string1, string2):
        return len(string1) >= 3 and len(string2) >= 3 and (Counter(string1.lower()) == Counter(string2.lower()))
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
    return count <= 3