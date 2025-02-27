def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[22:83].lower()
    for i in range(len(substring) - 33):
        for j in range(2, 4):
            candidate = substring[i:i + j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes