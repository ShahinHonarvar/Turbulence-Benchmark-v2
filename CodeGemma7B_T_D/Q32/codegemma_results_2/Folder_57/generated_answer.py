def insert_after_character(string):
    W = 'w'
    S = 's'
    new_string = string
    for character in new_string:
        if character == S:
            right = new_string[new_string.index(S) + 1:]
            new_string = new_string[:new_string.index(S) + 1] + W + right
    return new_string