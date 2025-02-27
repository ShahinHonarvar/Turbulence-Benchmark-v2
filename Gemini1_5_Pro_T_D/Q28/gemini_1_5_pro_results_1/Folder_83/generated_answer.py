def return_nth_smallest_ascii(text):
    relevant_chars = sorted([ord(text[i]) for i in range(max(0, 30), min(len(text), 71))])
    return chr(relevant_chars[14]) if len(relevant_chars) > 14 else None