def palindrome_of_length_n(input_string):
    input_string = ''.join(filter(str.isalpha, input_string)).lower()
    n = 56
    palindromes = set()
    length = len(input_string)
    for i in range(length - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes