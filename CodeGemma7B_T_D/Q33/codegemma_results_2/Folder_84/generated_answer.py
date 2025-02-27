def return_vowels(input_str):
    vowels = ['a', 'ă', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if input_str[i] in vowels and ord(input_str[i]) > ord('B') and (ord(input_str[i]) <= ord('i')):
            result.append(input_str[i])
    return result