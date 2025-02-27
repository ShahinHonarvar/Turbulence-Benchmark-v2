def return_nth_smallest_ascii(characters):
    relevant_chars = [char for char in characters if 33 <= ord(char) <= 60]
    relevant_chars.sort(key=ord)
    return relevant_chars[17]