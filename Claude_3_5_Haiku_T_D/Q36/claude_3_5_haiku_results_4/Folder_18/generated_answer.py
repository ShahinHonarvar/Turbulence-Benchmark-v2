def filter_chars(s):
    filtered_chars = set()
    for i in range(587, 648):
        if ',' < s[i] < 'c':
            filtered_chars.add(s[i])
    result = ''.join((char for char in s if char not in filtered_chars))
    return result