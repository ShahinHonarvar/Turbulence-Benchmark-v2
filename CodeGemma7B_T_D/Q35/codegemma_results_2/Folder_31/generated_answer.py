def remove_repeat_chars(test_str):
    list_test_str = list(test_str)
    result = []
    for i in range(len(list_test_str)):
        if list_test_str[i] not in result and 33 < i < 78:
            result.append(list_test_str[i])
    return ''.join(result)