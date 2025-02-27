def return_vowels(my_str):
    return [char for char in my_str[11:61] if char in 'AEIOUaeiou' and char > 'M' and (char <= 'W')]