def all_substring_of_size_n(s):
    char_list = [char for char in s]
    result = []
    for i in range(len(char_list) - 26):
        temp = ''.join(char_list[i:i + 27])
        if temp not in result:
            result.append(temp)
    if not result:
        return []
    else:
        return result