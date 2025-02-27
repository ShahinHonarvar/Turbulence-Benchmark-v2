def return_nth_smallest_ascii(s):
    relevant_chars = sorted(list(set([c for i, c in enumerate(s) if i >= 0 and i <= 87])))
    if len(relevant_chars) >= 14:
        return relevant_chars[13]
    else:
        return None