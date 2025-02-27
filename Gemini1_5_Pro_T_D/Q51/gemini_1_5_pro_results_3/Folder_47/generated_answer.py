from collections import Counter

def if_contains_anagrams(list_of_strings):

    def is_anagram(first_string, second_string):
        return Counter(first_string.lower()) == Counter(second_string.lower())
    number_of_anagrams = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and is_anagram(list_of_strings[i], list_of_strings[j]):
                number_of_anagrams += 1
    return number_of_anagrams <= 366