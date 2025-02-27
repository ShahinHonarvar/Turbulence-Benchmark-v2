def insert_before_character(s):
    s_list = list(s)
    new_s = []
    for i in range(1, len(s_list)):
        if s_list[i] == ' ':
            new_s.append(' ')
        new_s.append(s_list[i])
    return ''.join(new_s)