def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    n = 76
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + n, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes