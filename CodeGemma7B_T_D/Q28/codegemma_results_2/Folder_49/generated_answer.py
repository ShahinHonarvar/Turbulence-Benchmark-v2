def return_nth_smallest_ascii(text):

    def nth_smallest_ascii(text, index):
        keys = text[index:index + 20]
        sorted_keys = sorted(keys)
        return sorted_keys[index]
    return nth_smallest_ascii(text, 9)