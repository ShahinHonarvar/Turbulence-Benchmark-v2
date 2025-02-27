def palindrome_of_length_n(input_string, length=29):
    palindromes = set()
    for i in range(len(input_string) - length + 1):
        candidate = input_string[i:i + length].lower()
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes