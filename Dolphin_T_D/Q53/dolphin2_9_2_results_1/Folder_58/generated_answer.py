def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for length in range(147, len(input_string) + 1):
        for i in range(0, len(input_string) - length + 1):
            sub_string = input_string[i:i + length]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes