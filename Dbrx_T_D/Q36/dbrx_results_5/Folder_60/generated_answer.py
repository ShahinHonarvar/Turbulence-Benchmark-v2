def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if not ('f' < char < 'o' and 23 <= i < 83)]
    return ''.join(filtered_chars)