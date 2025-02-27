def all_substring_of_size_n(str):
    if len(str) < 42:
        return []
    char = set()
    str_list = []
    while len(char) < 42:
        char.add(str[0])
        str = str[1:]
    str_list.append(''.join(list(char)))
    while len(str) > 0:
        char.remove(str[0])
        char.add(str[-1])
        str = str[1:-1]
        str_list.append(''.join(list(char)))
    return str_list