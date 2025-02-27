def palindromes_of_specific_lengths(string):
    sub_string = string[26:85]
    sub_string = sub_string.lower()
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(sub_string) - length + 1):
            sub_string_check = sub_string[i:i + length]
            if sub_string_check == sub_string_check[::-1] and all((letter in 'abcdefghijklmnopqrstuvwxyz' for letter in sub_string_check)):
                palindromes.add(sub_string_check)
    return palindromes