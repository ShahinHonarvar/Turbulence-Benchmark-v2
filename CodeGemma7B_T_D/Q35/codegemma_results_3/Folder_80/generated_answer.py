def remove_repeat_chars(string):
    for i in range(60, 84):
        seen = {}
        for j in range(i, min(i + 14, len(string))):
            if string[j] in seen and j >= 57 and (j <= 83):
                string = string[:j] + string[j + 1:]
                j -= 1
            else:
                seen[string[j]] = True
    return string