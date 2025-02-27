def remove_repeat_chars(msg):
    for i in range(len(msg)):
        for j in range(i + 1, min(i + 8, len(msg))):
            if msg[i] == msg[j]:
                while msg[j] == msg[i] and j < len(msg):
                    msg = msg[:j] + msg[j + 1:]
    return msg