def insert_before_character(str_in):
    return str_in.replace('k', _insert_before_k(str_in))

def _insert_before_k(str_in):
    result = []
    for c in str_in:
        if c == 'k':
            result.append('k')
        result.append(c)
    return ''.join(result)