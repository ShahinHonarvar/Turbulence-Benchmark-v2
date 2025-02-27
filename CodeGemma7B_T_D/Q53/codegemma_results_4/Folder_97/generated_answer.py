def palindrome_of_length_at_least_n(input_string):
    all_palindromes = set()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            substring = input_string[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 138:
                all_palindromes.add(substring.casefold())
    return all_palindromes