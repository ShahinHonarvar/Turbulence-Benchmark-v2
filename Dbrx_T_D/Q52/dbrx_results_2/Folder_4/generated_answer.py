def palindrome_of_length_n(input_string, length=15):
    input_string = ''.join((e for e in input_string.lower() if e.isalpha()))
    palindromes = set()
    for i in range(len(input_string) - length + 1):
        if input_string[i:i + length] == input_string[i:i + length][::-1]:
            palindromes.add(input_string[i:i + length])
    return palindromes