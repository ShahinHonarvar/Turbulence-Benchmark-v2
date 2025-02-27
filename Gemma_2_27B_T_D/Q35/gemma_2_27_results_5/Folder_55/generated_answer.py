from collections import Counter

def remove_repeat_chars(text):
    counts = Counter(text[10:100])
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text