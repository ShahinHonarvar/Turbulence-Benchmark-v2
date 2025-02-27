def return_vowels(str):
    vowels2 = []
    for letter in str:
        if letter in 'aeiouAEIOU' and ord(letter) >= ord('h') and (ord(letter) <= ord('p')) and (ord(letter) > ord('9')):
            vowels2.append(letter)
    return vowels2