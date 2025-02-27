def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[26:88]
    palindromes = set()
    for i in range(len(substring) - 52):
        for length in range(52, 57):
            if length > len(substring) - i:
                continue
            temp_substring = substring[i:i + length]
            if temp_substring.lower() == temp_substring[::-1].lower():
                palindromes.add(temp_substring)
    return palindromes