def palindrome_of_length_at_least_n(input_string):
    palindromes_set = set()
    for i in range(len(input_string)):
        for j in range(i + 80, len(input_string)):
            substring = input_string[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes_set.add(substring)
    return palindromes_set