def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for idx, char in enumerate(s):
        if 50 <= idx < 77 and char.lower() in vowels and ('#' < char.lower() <= 'r'):
            result.append(char)
    return result