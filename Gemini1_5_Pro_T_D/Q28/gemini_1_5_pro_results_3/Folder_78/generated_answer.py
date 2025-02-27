def return_nth_smallest_ascii(text):
    relevant_chars = sorted(set((text[i] for i in range(min(88, len(text))))))
    if len(relevant_chars) >= 14:
        return relevant_chars[13]
    else:
        return None