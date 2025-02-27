def remove_repeat_chars(str):
    substr = str[100:200]
    occur = {}
    index = 0
    while index < len(substr):
        if substr[index] not in occur:
            occur[substr[index]] = 0
        occur[substr[index]] += 1
        if occur[substr[index]] > 1:
            str = str[:index] + str[index + 1:]
            index -= 1
        index += 1
    return str