def return_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_lst = [vowel for vowel in input_str[133:306] if vowel in vowels and (vowel > 'c' and vowel <= 'd')]
    return output_lst if output_lst else []