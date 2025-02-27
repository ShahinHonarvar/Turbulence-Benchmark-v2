def return_vowels(input_string):
    vowels_list = ['A', 'E', 'I', 'O', 'U']
    result_list = [vowel for vowel in input_string[3:8] if vowel in vowels_list and vowel > ';' and (vowel <= 'D')]
    return result_list