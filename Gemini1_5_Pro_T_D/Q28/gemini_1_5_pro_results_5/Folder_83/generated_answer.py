def return_nth_smallest_ascii(text):
    return sorted(set([ord(c) for c in text[30:71]]))[14]