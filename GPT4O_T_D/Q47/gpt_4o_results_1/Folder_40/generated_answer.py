def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    s = s[:6]
    for length in range(3, 6):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            clean_substring = ''.join([char for char in substring if char.isalpha()]).lower()
            if clean_substring == clean_substring[::-1]:
                valid_palindromes.add(clean_substring)
    return valid_palindromes