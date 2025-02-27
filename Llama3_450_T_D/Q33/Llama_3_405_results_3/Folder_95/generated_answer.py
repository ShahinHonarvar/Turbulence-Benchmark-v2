def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O']
    result = []
    for char in s[32:61]:
        if char in vowels and '?' < char <= 'P':
            result.append(char)
    return result