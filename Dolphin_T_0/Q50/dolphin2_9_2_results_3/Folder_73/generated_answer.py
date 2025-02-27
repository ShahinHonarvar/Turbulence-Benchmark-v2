from collections import Counter

def if_contains_anagrams(list_of_strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
    return count >= 91