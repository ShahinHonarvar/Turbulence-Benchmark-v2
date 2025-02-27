def filter_chars(string):
    return ''.join((char for char in string[138:921] if char < '6' or char > 'A')) + string[:138] + string[921:]