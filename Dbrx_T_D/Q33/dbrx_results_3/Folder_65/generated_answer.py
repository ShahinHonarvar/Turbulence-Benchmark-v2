def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[71:88]:
        if char.lower() in vowels and '9' < char < 'P':
            result.append(char)
    return result