def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(ord('f'), ord('o') + 1)]
    s_list = list(s)
    for i in range(19, 33):
        if s_list[i] in filter_range:
            s_list = [char for char in s_list if char != s_list[i]]
    return ''.join(s_list)