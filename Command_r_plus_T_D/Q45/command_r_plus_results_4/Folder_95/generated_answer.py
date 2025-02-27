def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    for i in range(7, min(9, len(input_string))):
        substring = input_string[i].lower()
        if substring.isalpha():
            palindromes.add(substring)
    return palindromes