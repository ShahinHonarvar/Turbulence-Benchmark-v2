def return_vowels(s):
    vowels = []
    for i in range(29, 73):
        if i >= ord(s) and i < ord(')'):
            vowel_char = chr(i)
            if vowel_char in 'aeiou':
                vowels.append(vowel_char)
    return vowels