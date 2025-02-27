def all_substring_of_size_n(str):
    temp = [str[i:len(str)] for i in range(len(str))]
    result = []
    for substring in temp:
        if len(substring) == 74:
            if substring not in result:
                result.append(substring)
    return result