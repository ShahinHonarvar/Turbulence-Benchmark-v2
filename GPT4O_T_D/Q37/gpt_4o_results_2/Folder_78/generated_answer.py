def filter_chars(s):
    to_remove = set()
    for ch in s[75:100]:
        if '8' <= ch <= 'e':
            to_remove.add(ch)
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result