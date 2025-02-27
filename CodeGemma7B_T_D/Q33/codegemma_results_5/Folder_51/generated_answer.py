def return_vowels():
    vowels = 'aeiouAEIOU'
    the_string = input()
    the_character_list = list(the_string)
    count = 0
    vowel_list = []
    for letter in the_character_list:
        if letter in vowels and letter > 'M' and (letter <= 'X'):
            vowel_list.append(letter)
        count += 1
    return vowel_list