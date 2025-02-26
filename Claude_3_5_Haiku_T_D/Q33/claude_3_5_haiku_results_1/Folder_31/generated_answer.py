def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in s:
        if char in vowels and 65 <= ord(char) < 70 and (ord(char) > ord('%')) and (ord(char) <= ord('G')):
            result.append(char)
    return result