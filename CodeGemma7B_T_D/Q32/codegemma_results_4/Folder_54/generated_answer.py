def insert_after_character(str):
    return re.sub('M(.*?)', 'M\\\\1f', str)