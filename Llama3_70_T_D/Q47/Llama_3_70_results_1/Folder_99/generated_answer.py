def palindromes_of_specific_lengths(input_string):
    input_string = input_string[127:289].lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 119, min(i + 142, len(input_string) + 1)):
            substring = input_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes