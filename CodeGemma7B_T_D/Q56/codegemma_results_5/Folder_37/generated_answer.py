def all_substring_of_size_n(str1):
    result = []
    for i in range(len(str1)):
        for j in range(i + 65, len(str1) + 1):
            substring = str1[i:j]
            if len(substring) == 65 and (not substring in result):
                result.append(substring)
    return result if result else []