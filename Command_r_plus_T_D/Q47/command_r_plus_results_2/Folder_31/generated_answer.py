def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:84]
    for length in range(37, 61):
        for start in range(len(substring) - length + 1):
            end = start + length
            sub_sub_string = substring[start:end]
            if sub_sub_string.isalpha() and sub_sub_string.lower() == sub_sub_string[::-1].lower():
                palindromes.add(sub_sub_string)
    return palindromes