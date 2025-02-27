def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    substring = input_string[4:9].lower()
    for i in range(len(substring)):
        for j in range(i + 6, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes