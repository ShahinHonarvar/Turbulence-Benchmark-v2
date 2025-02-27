def filter_chars(given_string):
    for i, char in enumerate(given_string):
        if 90 < i < 97 and char > 'j' and (char < 'w'):
            filtered_string = given_string[:i] + given_string[i + 1:]
            given_string = filtered_string
    return given_string