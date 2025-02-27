def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = []
    for char in s[32:61]:
        if char in vowels and '?' < char <= 'P':
            result.append(char)
    return result