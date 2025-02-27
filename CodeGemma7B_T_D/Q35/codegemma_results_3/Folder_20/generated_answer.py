def remove_repeat_chars(str_input):
    str_input = str_input[:27] + ''.join([l for l in str_input[27:96] if str_input.index(l) == str_input.rindex(l)]) + str_input[96:]
    return str_input