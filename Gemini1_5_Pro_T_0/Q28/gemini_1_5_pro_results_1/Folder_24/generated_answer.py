def return_nth_smallest_ascii(text):
    return sorted(list(set([text[i] for i in range(34, 82)])))[11]