def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[2:9].lower()
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            substring_slice = substring[i:j]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes