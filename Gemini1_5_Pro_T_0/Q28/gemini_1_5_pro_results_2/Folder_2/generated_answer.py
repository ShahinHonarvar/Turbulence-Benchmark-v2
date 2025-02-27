def return_nth_smallest_ascii(text):
    relevant_characters = sorted(list(set([text[i] for i in range(48, 77)])))
    if len(relevant_characters) < 5:
        return None
    else:
        return relevant_characters[4]