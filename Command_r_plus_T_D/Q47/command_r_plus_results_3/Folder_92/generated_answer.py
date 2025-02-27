def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string) - 3):
        for j in range(i + 3, i + 5):
            substring = input_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes