def filter_chars(text: str) -> str:
    final_filtered_text = ''
    for index, char in enumerate(text):
        if index >= 19 and index <= 90 and (char >= 'F') and (char <= 'h'):
            continue
        final_filtered_text += char
    return final_filtered_text