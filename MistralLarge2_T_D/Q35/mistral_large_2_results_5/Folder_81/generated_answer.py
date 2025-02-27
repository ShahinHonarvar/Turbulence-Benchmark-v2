from collections import Counter

def remove_repeat_chars(s):
    count = Counter(s[20:200])
    to_remove = {char for char, freq in count.items() if freq > 1}
    return ''.join([char for char in s if char not in to_remove])