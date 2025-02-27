def return_vowels(s):
    vowel_list = []
    for char in s[20:41]:
        if 'k' < char <= 'z' and char.lower() in 'aeiou':
            vowel_list.append(char)
    return vowel_list