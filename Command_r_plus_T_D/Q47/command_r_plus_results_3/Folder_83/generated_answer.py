def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[74:96]
    for i in range(len(substring) - 6):
        for length in range(7, 10):
            if length > len(substring) - i:
                break
            temp_substring = substring[i:i + length]
            if temp_substring.isalpha() and temp_substring.lower() == temp_substring[::-1].lower():
                palindromes.add(temp_substring)
    return palindromes