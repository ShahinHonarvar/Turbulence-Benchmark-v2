def return_vowels(text):
    left_idx = 12
    right_idx = 39
    vowels = 'aeiou'
    found = []
    for char in text[left_idx:right_idx]:
        if 'a' <= char <= 'z' and char in vowels:
            found.append(char)
    return found