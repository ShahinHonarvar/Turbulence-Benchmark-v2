def return_nth_smallest_ascii(text):
    relevant_characters = sorted(set((text[i] for i in range(min(46, len(text))))))
    if len(relevant_characters) >= 10:
        return relevant_characters[9]
    else:
        return None