def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[23:98].lower()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            sub_substring = substring[i:i + length]
            if sub_substring == sub_substring[::-1] and sub_substring.isalpha():
                palindromes.add(sub_substring)
    return palindromes