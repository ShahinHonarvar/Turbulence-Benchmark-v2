def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[26:96]
    for i in range(len(substring) - 49):
        for length in range(49, 52):
            if length > len(substring) - i:
                continue
            temp_substring = substring[i:i + length]
            if temp_substring.lower() == temp_substring[::-1].lower():
                palindromes.add(temp_substring)
    return palindromes