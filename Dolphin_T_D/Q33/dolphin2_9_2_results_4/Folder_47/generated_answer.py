def return_vowels(s):
    vowels = 'aeiou'
    returned_list = []
    for char in s[23:38]:
        if char.lower() in vowels:
            if char.lower() > 'n' and char.lower() <= 'k':
                if char.isalpha():
                    returned_list.append(char)
    return returned_list