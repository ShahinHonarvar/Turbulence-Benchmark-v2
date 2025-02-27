def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    L = ord('L')
    d = ord('d')
    result = [s[i] for i in range(23, 75) if ord(s[i]) > L and ord(s[i]) <= d and (s[i] in vowels)]
    return result