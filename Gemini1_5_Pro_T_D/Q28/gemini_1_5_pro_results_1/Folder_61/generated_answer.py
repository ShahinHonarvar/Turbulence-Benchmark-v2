def return_nth_smallest_ascii(text):
    return sorted(list(set([text[i] for i in range(0, min(10, len(text)))])))[9]