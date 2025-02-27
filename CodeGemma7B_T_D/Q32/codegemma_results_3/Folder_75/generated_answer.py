def insert_after_character(txt):
    output = txt
    for i in range(len(txt)):
        if txt[i] == 'U':
            output = output[:i + 1] + 'q' + output[i + 1:]
    return output