def remove_repeat_chars(input_string):
    if len(input_string) <= 21:
        return input_string
    start_index = 21
    end_index = min(200, len(input_string))
    substring = input_string[start_index:end_index]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for i, char in enumerate(input_string):
        if i < start_index or i >= end_index or char not in repeat_chars:
            result.append(char)
    return ''.join(result)