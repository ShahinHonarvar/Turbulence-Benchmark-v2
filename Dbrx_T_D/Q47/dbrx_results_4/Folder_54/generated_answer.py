def palindromes_of_specific_lengths(input_string):
    input_string = input_string[27:78].lower()
    palindromes = {input_string[i:j] for i in range(len(input_string)) for j in range(i + 1, len(input_string) + 1) if j - i >= 18 and j - i <= 19 and (input_string[i:j] == input_string[i:j][::-1])}
    return palindromes