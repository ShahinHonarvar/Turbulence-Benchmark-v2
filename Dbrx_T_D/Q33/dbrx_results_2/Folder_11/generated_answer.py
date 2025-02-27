def return_vowels(text):
    vowels = []
    start_index = 29
    end_index = 73
    for char in text[start_index:end_index]:
        if 'c' < char <= '#':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels