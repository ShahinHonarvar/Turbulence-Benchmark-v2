def all_substring_of_size_n(string):
    all_substring = []
    for i in range(len(string) - 69):
        substring = string[i:i + 70]
        is_unique = True
        for sub in all_substring:
            if sub == substring:
                is_unique = False
                break
        if is_unique:
            all_substring.append(substring)
    return all_substring