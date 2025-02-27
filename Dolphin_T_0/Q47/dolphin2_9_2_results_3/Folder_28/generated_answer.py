def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(21, 33):
        for start_idx in range(32, 72 - length + 1):
            substring = s[start_idx:start_idx + length]
            if all((char in 'abcdefghijklmnopqrstuvwxyz' for char in substring.lower())):
                if substring.lower() == substring[::-1].lower():
                    valid_palindromes.add(substring)
    return valid_palindromes