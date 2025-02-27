def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[14:87].lower()
    for i in range(len(substring) - 50):
        for length in range(51, 61):
            if i + length > len(substring):
                break
            temp_substring = substring[i:i + length]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes