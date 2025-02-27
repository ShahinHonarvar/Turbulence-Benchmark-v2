def remove_repeat_chars(s):
    dict_f = dict()
    for i, v in enumerate(s):
        if i < 36 or i > 85:
            dict_f[v] = i
    string_inherit = ''
    for i, v in enumerate(s):
        if i < 36 or i > 85:
            if v in dict_f:
                string_inherit = string_inherit + s[dict_f[v]:]
            else:
                string_inherit = string_inherit + v
    return string_inherit