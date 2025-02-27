from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for count, string in enumerate(list_of_strings):
        for string2 in list_of_strings[count + 1:]:
            if len(string) >= 3 and len(string2) >= 3 and (Counter(string.lower()) == Counter(string2.lower())):
                anagram_count += 1
    return anagram_count <= 445