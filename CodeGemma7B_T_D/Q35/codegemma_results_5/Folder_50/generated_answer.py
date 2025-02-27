def remove_repeat_chars(given_string):
    unique_chars = set()
    result = list(given_string)
    for i in range(13, 76):
        if result[i] in unique_chars:
            while result[i] in result:
                result.remove(result[i])
        else:
            unique_chars.add(result[i])
    return ''.join(result)