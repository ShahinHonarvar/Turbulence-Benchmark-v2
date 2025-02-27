def filter_chars(s: str) -> str:
    filter_set = set(s[1:4])
    filter_set = filter_set - set((chr(i) for i in range(36, 64)))
    s_list = list(s)
    for i, c in enumerate(s_list):
        if c in filter_set:
            s_list[i] = ''
    return ''.join(s_list)