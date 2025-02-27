def return_vowels(s):
    vowels = []
    for i in range(36, 56):
        if i < len(s):
            char = s[i]
            if '+' < char <= '/':
                if char in 'AEIOUaeiou':
                    vowels.append(char)
    return vowels