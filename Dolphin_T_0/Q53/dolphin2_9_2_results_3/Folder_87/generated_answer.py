def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    n = 18
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + n, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes