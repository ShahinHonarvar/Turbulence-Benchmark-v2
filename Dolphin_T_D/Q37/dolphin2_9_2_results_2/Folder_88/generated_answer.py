def filter_chars(string):
    result = ''
    for char in range(len(string)):
        if char < 70 or char > 80 or (string[char] < '@' or string[char] > 'p'):
            result += string[char]
    return result