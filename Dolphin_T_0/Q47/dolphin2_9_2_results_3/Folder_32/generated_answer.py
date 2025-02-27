def palindromes_of_specific_lengths(s):
    palindromes = set()
    str_length = len(s)
    for i in range(str_length - 46, 44):
        sub_string = s[i:i + 47]
        for j in range(0, 47 - 42):
            temp_string = sub_string[j:j + 46]
            temp_string = ''.join(filter(str.isalpha, temp_string))
            temp_string = temp_string.lower()
            if temp_string == temp_string[::-1]:
                palindromes.add(temp_string)
    return palindromes