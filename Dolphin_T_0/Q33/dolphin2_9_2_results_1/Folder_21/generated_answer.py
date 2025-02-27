def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_string = my_string[464:574]
    result = [char for char in sub_string if char in vowels and 'a' < char <= 'g']
    return result