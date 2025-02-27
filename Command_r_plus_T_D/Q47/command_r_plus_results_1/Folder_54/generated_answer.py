def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[26:78].lower()
    palindromes = set()
    for i in range(len(substring) - 18):
        for j in range(3, 20):
            if substring[i:i + j] == substring[i:i + j][::-1] and substring[i:i + j].isalpha():
                palindromes.add(substring[i:i + j])
    return palindromes