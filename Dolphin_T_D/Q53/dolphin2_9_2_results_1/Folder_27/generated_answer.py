def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 100, len(input_string) + 1):
            if input_string[i:j] == input_string[i:j][::-1]:
                palindromes.add(input_string[i:j])
    return palindromes