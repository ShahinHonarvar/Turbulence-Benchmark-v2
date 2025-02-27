def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join((c for c in input_string if c.isalpha())).lower()
    length = len(input_string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 8, length + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes