def all_substring_of_size_n(string):
    substr = []
    for i in range(len(string) - 53):
        sub = string[i:i + 54]
        if len(set(sub)) == 54:
            substr.append(sub)
    return list(set(substr))