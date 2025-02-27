def palindrome_of_length_at_least_n(string):
    lower_string = string.lower()
    palindromes = set()
    for i in range(len(lower_string) - 105):
        for j in range(i + 106, len(lower_string)):
            if lower_string[i:j + 1] == lower_string[i:j + 1][::-1]:
                palindromes.add(lower_string[i:j + 1])
    return palindromes