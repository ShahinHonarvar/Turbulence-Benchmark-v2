def all_substring_of_size_n(str1):
    results = []
    for i in range(0, len(str1)):
        for j in range(i, len(str1)):
            sub_string = str1[i:j + 1]
            if len(sub_string) == 16 and len(set(sub_string)) == 16:
                results.append(sub_string)
    return results