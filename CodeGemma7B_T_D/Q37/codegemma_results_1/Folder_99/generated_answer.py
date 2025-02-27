def filter_chars(message):
    for i in range(373, 902):
        if message[i] >= 'T' and message[i] <= 'h':
            while message.find(message[i]) != -1:
                message = message.replace(message[i], '', 1)
    return message