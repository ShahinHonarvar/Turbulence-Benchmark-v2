def palindromes_of_specific_lengths(input_string):
    input_string = input_string[29:99].lower()
    valid_palindromes = set()
    for i in range(len(input_string)):
        for j in range(6, 10):
            if i + j <= len(input_string):
                substring = input_string[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    valid_palindromes.add(substring)
    return valid_palindromes