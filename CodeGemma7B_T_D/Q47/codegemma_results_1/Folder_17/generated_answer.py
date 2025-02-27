from string import ascii_lowercase

def palindromes_of_specific_lengths(str):
    uppercase_letters = {letter: letter.upper() for letter in ascii_lowercase}
    palindromes = set()
    for i in range(22, 96):
        for j in range(52, 56):
            if j + i >= len(str):
                continue
            substring = str[i:i + j]
            is_palindrome = all((letter in uppercase_letters and uppercase_letters[letter] == substring[j - k - 1] or letter.upper() == substring[j - k - 1] for k, letter in enumerate(substring)))
            if is_palindrome:
                palindromes.add(substring)
    return palindromes