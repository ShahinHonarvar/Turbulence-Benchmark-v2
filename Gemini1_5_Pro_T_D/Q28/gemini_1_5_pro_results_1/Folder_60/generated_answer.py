def return_nth_smallest_ascii(text):
    sorted_ascii = sorted(set((ord(c) for c in text[36:80])))
    return chr(sorted_ascii[11])