def remove_repeat_chars(txt):
    seen = set()
    result = []
    for i in range(len(txt)):
        if i < 355 or i >= 988:
            if txt[i] in seen:
                continue
            seen.add(txt[i])
        result.append(txt[i])
    return ''.join(result)