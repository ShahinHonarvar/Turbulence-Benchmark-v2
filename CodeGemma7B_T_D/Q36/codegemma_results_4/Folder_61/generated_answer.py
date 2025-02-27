def filter_chars(text):
    filtered_text = [char for char in text if char not in text[3:9] or char < '*' or char > 'E']
    return ''.join(filtered_text)