def return_nth_smallest_ascii(text):
    return sorted([ord(char) for char in text[8:66] if char not in text[8:66][:6]])[5]