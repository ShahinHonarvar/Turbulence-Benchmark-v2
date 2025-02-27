def return_nth_smallest_ascii(text):
    subtext = text[17:46]
    subtext = sorted(subtext, key=ord)
    return subtext[6]