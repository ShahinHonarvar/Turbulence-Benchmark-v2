def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[22:83].lower()
    for i in range(len(substring) - 33):
        for length in range(32, 35):
            if i + length > len(substring):
                break
            current_substring = substring[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes