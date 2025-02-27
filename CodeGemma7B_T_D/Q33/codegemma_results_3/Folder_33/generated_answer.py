def return_vowels(str1):
    vowels = []
    for i, char in enumerate(str1):
        if 163 <= i < 771 and char in 'AEIOUaeiou':
            if char > ':' and char <= 'E':
                vowels.append(char)
    return vowels