def return_vowels(s):
    vowels = []
    for char in s[17:65]:
        if 'U' < char <= '{':
            if char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels