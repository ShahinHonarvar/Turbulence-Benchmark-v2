def filter_chars(s):
    indices_to_check = set()
    for i in range(673, 709):
        if i < len(s):
            char = s[i]
            if 'X' < char < '}':
                indices_to_check.add(char)
    result = [char for char in s if char not in indices_to_check]
    return ''.join(result)