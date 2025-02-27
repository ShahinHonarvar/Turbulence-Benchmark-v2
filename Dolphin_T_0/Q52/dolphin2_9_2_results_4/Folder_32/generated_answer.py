def palindrome_of_length_n(input_string):
    n = 113
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(substring) == n:
            lower_substring = substring.lower()
            if lower_substring == lower_substring[::-1]:
                palindromes.add(substring)
    return palindromes