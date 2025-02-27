def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[14:73].lower()
    palindromes = set()
    for length in range(19, 56):
        for start in range(len(substring) - length + 1):
            end = start + length
            temp_substring = substring[start:end]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes