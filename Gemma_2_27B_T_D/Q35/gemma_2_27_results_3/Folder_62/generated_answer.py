from collections import Counter

def remove_repeat_chars(text):
    char_counts = Counter(text[50:92])
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text