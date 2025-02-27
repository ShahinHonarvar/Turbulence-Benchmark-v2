from string import ascii_uppercase, digits

def filter_chars(txt):
    filtered = ''
    for i in range(len(txt)):
        if i < 40 or i > 63:
            filtered += txt[i]
    for c in txt[40:63]:
        if c > '7' and c < 'H':
            filtered = filtered.replace(c, '')
    return filtered