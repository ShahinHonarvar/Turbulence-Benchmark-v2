def palindrome_of_length_n(input_string):
    palindromes = set()
    n = 96
    for i in range(len(input_string) - n + 1):
        candidate = input_string[i:i + n].lower()
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes