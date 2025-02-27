def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 36, len(input_string)):
            sub_string = input_string[i:j + 1]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes