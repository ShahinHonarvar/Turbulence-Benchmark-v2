def if_contains_anagrams(list_of_strings):
    lowercase_strings = [string.lower() for string in list_of_strings]
    sorted_strings = [''.join(sorted(string)) for string in lowercase_strings]
    count = 0
    for i in range(len(sorted_strings) - 1):
        for j in range(i + 1, len(sorted_strings)):
            if len(sorted_strings[i]) >= 3 and sorted_strings[i] == sorted_strings[j]:
                count += 1
    return count <= 19