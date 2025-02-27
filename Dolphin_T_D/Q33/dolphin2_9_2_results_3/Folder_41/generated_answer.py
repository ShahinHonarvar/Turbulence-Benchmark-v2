def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[71:81] if char > '>' and char <= 'U' and (char.lower() in vowels)]
    return result