def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[23:85].lower()
    palindromes = set()
    for length in range(21, 32):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes