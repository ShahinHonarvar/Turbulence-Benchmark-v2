from collections import Counter

def if_contains_anagrams(list_of_strings):

    def is_anagram(first_string, second_string):
        return len(first_string) >= 3 and len(second_string) >= 3 and (Counter(first_string.lower()) == Counter(second_string.lower()))
    number_of_anagrams = 0
    for first_index in range(len(list_of_strings) - 1):
        for second_index in range(first_index + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[first_index], list_of_strings[second_index]):
                number_of_anagrams += 1
    return number_of_anagrams <= 52