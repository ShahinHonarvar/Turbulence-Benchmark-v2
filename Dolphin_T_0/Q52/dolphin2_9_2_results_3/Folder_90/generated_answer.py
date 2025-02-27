def palindrome_of_length_n(string):
    lower_case_string = string.lower()
    palindromes = set()
    n = 318
    for i in range(len(lower_case_string) - n + 1):
        sub_string = lower_case_string[i:i + n]
        if sub_string == sub_string[::-1] and all((letter.isalpha() for letter in sub_string)):
            palindromes.add(sub_string)
    return palindromes