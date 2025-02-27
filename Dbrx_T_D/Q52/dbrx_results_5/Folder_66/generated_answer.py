def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 24):
        for j in range(26):
            substring = input_string[i:i + 25]
            if input_string[i + j] == input_string[i + j + 24] and all((c == input_string[i + k] for k in range(1, 24) for c in substring[i + k:i + k + 2])):
                palindromes.add(substring)
    return palindromes