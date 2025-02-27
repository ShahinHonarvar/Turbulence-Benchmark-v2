def all_substring_of_size_n(string):
    list_of_substr = []
    for i in range(len(string) - 48):
        substring = string[i:i + 49]
        if len(substring) == len(set(substring)) and substring not in list_of_substr:
            list_of_substr.append(substring)
    return list_of_substr