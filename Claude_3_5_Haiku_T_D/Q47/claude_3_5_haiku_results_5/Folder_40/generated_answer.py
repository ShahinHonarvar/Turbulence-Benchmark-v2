def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[:6].lower()
    for length in range(3, 6):
        for start in range(len(substring) - length + 1):
            current_substring = substring[start:start + length]
            if all((char.isalpha() for char in current_substring)):
                if current_substring == current_substring[::-1]:
                    palindromes.add(current_substring)
    return palindromes