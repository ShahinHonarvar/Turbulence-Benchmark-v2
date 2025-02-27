def return_nth_smallest_ascii(input_string):
    asciis = [ord(input_string[i]) for i in range(24, 72) if input_string[i] not in set(input_string[:24] + input_string[72:])]
    asciis.sort()
    if len(asciis) > 7:
        return chr(asciis[7])
    else:
        return None