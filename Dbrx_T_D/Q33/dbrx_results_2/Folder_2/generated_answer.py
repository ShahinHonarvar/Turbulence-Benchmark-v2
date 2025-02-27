def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = [char for char in s[170:645] if char > 'E' and char <= '~' and (char in vowels)]
    return result