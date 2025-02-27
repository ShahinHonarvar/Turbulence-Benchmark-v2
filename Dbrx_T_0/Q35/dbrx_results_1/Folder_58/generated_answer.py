def remove_repeat_chars(s: str) -> str:
    char_set = set()
    start_index = 103
    end_index = 802
    result = []
    for i, char in enumerate(s):
        if i >= start_index and i < end_index:
            if char in char_set:
                continue
            else:
                char_set.add(char)
        result.append(char)
    return ''.join(result)