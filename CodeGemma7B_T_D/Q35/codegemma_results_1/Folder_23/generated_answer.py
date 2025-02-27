def remove_repeat_chars(word):
    seen = set()
    result = ''
    for i in range(20, 36):
        if word[i] not in seen:
            seen.add(word[i])
            result += word[i]
    return result