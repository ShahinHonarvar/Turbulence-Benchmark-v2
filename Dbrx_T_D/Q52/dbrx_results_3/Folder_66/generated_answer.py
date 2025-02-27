def palindrome_of_length_n(input_string):
    n = 25
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        candidate = input_string[i:i + n]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes