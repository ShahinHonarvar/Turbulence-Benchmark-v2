def remove_repeat_chars(text):
    store = set()
    result = ''
    for i in range(36, 52):
        if text[i] not in store:
            result += text[i]
            store.add(text[i])
    return result