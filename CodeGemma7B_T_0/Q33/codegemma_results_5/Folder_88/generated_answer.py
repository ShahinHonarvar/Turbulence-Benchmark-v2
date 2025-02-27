def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(70, 76):
        if text[i] in vowels and (ord(text[i]) > ord('2') and ord(text[i]) <= ord(':')) and (text[i] not in result):
            result.append(text[i])
    return result