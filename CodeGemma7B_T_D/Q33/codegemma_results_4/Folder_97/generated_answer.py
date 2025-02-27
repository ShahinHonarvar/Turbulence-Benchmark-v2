def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_list = []
    for i in range(328, 455):
        if string[i].lower() in vowels and string[i] <= 'z' and (string[i] > '<'):
            output_list.append(string[i])
    return output_list