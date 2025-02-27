def filter_chars(text):
    filtered_text = text[:12] + ''.join((c for c in text[12:78] if c not in (':', 'L'))) + text[78:]
    return filtered_text