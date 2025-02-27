def remove_repeat_chars(text):
    result = text[:40]
    for index, char in enumerate(text[40:200]):
        if char in result:
            continue
        elif result.count(char) > 0:
            result = ''.join((c for c in result if c != char))
        else:
            result += char
    result += text[200:]
    return result