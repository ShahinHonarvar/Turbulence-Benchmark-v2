def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [my_string[i] for i in range(202, 872) if 3 < ord(my_string[i]) <= ord('>') and my_string[i] in vowels]
    return result