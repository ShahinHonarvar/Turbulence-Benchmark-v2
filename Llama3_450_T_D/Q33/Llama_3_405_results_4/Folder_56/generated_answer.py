def return_vowels(s):
    vowel_list = []
    for i in range(15, 86):
        if i < len(s):
            char = s[i]
            if '@' < char <= '~' and char.lower() in 'aeiou':
                vowel_list.append(char)
    return vowel_list