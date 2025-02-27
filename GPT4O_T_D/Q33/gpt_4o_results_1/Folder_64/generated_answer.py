def return_vowels(s):
    vowels = 'aeiouAEIOU'
    selected_vowels = []
    for char in s[1:7]:
        if char in vowels and 'F' < char <= 'j':
            selected_vowels.append(char)
    return selected_vowels