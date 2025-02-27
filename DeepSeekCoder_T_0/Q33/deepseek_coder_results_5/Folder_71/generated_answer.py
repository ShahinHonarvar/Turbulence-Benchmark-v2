def return_vowels(s):
    vowels = []
    for char in s[36:56]:
        if '+' < char <= '/':
            if char in 'AEIOUaeiou':
                vowels.append(char)
    return vowels