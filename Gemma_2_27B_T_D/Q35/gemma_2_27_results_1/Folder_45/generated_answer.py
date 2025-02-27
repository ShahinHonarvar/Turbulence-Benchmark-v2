from collections import Counter

def remove_repeat_chars(text):
    char_counts = Counter(text[40:200])
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text