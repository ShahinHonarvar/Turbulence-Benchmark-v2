def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = string[23:85]
    answer = []
    for letter in new_string:
        if letter in vowels and letter > 'W' and (letter <= 'v'):
            answer.append(letter)
    if answer == []:
        return []
    else:
        return answer