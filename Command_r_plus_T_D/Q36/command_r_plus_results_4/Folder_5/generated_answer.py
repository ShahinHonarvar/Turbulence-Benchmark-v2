def filter_chars(input_string: str) -> str:
    filter_range = list(range(56, 67))
    filter_chars = [chr(i) for i in range(ord('f') + 1, ord('|'))]
    filtered_string = input_string
    for char in filter_chars:
        index = input_string.find(char)
        while index in filter_range and index != -1:
            filtered_string = filtered_string.replace(char, '', 1)
            index = input_string.find(char, index + 1)
    return filtered_string