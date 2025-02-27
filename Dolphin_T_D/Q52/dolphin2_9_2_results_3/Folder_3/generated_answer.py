def palindrome_of_length_n(input_string):
    n = 100
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        sub_string = input_string[i:i + n]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes