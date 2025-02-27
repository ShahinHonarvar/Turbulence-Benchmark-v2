def filter_chars(s):
    filtered_str = []
    for char in s:
        if char > 'V' and char < 'j' and (ord(char) not in range(69, 97)):
            filtered_str.append(char)
    return ''.join(filtered_str)