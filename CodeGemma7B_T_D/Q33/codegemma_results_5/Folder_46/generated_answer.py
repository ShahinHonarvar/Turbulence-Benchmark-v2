def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = []
    for i in range(10, 83):
        if string[i] in vowels and string[i] > '%' and (string[i] <= 'e'):
            answer.append(string[i])
    return answer