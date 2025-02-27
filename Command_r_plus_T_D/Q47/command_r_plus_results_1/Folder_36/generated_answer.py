def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[123:284].lower()
    palindromes = set()
    for i in range(len(substring) - 114):
        for length in range(115, 135):
            if i + length > len(substring):
                break
            temp_substring = substring[i:i + length]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes