def all_substring_of_size_n(string):
    lst = []
    for i in range(len(string)):
        for j in range(i + 93, len(string)):
            substring = string[i:j + 1]
            if len(substring) == 93 and (not substring in lst):
                lst.append(substring)
    return lst