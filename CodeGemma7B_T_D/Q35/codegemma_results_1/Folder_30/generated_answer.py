from collections import Counter

def remove_repeat_chars(str):
    counter = Counter(str)
    for char in counter.most_common():
        if counter[char] > 1 and char in str[22:24]:
            str = str.replace(char, '')
    return str