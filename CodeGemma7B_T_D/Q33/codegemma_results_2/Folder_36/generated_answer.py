def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for char in text[604:949]:
        if char in vowels and 'N' < char <= 'U':
            vowel_list.append(char)
    return vowel_list