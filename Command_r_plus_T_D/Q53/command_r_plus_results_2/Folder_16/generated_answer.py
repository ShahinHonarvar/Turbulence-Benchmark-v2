def palindrome_of_length_at_least_n(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 118):
        substring = input_string[i:i + 119]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes