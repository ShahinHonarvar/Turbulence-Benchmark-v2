def remove_repeat_chars(text):
    i = 0
    j = 0
    occurances = 0
    result = []
    while i < len(text):
        if bool(text[i].lower()) and 50 <= i < 200:
            if text[i] == text[j]:
                occurrences += 1
            else:
                occurrences = 0
            if occurrences <= 1:
                result.append(text[i])
                j = i
        i += 1
    return ''.join(result)