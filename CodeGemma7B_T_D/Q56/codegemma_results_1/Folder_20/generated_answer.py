def all_substring_of_size_n(str):
    size = 50
    list_substring = []
    for i in range(len(str)):
        for j in range(i + size, len(str) + 1):
            substring = str[i:j]
            if len(substring) == size:
                if substring not in list_substring:
                    list_substring.append(substring)
    list_substring.sort()
    return list_substring