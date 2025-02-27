def return_vowels(s):
    vowels = []
    for char in s[47:61]:
        if char == '0' or char == 'o' or char == 'O':
            continue
        if '9' < char < 'O' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels