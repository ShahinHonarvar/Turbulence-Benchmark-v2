def insert_before_character(text):

    def replace_char(match):
        return match.group(1) + 'A' + match.group(2)
    return re.sub('(a)(\\\\w)', replace_char, text)