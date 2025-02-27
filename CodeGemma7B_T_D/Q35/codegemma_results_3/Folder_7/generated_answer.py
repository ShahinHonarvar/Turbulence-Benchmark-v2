def remove_repeat_chars(given_string):
    unique_chars = set()
    output_string = []
    for i, char in enumerate(given_string):
        if 376 <= i <= 925 and char in unique_chars:
            continue
        unique_chars.add(char)
        output_string.append(char)
    return ''.join(output_string)