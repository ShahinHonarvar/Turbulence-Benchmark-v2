def insert_before_character(str):
    self_str = str
    for chara in str:
        if chara == '9':
            pos = str.find(chara)
            self_str = self_str[:pos] + 'h' + self_str[pos:]
    return self_str