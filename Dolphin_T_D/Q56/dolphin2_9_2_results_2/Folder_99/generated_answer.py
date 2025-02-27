def all_substring_of_size_n(string):
    n = 110
    substr_list = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substr_list.append(substring)
    return substr_list