def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    output = []
    for char in s[17:65]:
        if 'U' < char <= '{':
            if char in vowels:
                output.append(char)
    return output