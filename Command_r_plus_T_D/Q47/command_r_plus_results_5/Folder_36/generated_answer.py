def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[123:284]
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes