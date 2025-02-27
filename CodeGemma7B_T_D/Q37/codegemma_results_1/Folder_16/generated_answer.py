from string import ascii_uppercase

def filter_chars(given_string):
    final_string = ''
    for i, j in enumerate(given_string):
        if (i >= 225 and i <= 381) and j.upper() in ascii_uppercase[13:25]:
            continue
        final_string += j
    return final_string