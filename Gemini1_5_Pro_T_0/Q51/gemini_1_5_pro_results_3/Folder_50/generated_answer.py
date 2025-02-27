from collections import Counter

def if_contains_anagrams(list_of_strings):
    lowercase_strings = [string.lower() for string in list_of_strings]
    filtered_strings = [string for string in lowercase_strings if len(string) >= 3]
    count = 0
    for i in range(len(filtered_strings) - 1):
        for j in range(i + 1, len(filtered_strings)):
            if Counter(filtered_strings[i]) == Counter(filtered_strings[j]):
                count += 1
    return count <= 47