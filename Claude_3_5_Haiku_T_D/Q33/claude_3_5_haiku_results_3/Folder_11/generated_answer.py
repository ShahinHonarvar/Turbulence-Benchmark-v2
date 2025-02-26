def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(29, 73):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and ord(char) > ord('#') and (ord(char) <= ord('(')):
                result.append(char)
    return result