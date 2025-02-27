def remove_repeat_chars(String):
    count = {}
    for i in range(13, 91):
        if String[i] in count:
            count[String[i]] += 1
        else:
            count[String[i]] = 1
    for key in count:
        if count[key] > 1:
            String = String.replace(key, '')
    return String