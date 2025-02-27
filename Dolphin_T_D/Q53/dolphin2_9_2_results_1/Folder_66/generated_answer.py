def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes_set = set()
    for i in range(len(input_string)):
        for j in range(i + 75, len(input_string)):
            substring = input_string[i:j + 1]
            if substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set