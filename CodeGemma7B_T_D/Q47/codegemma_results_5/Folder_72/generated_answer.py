from string import ascii_lowercase as letters
            from itertools import product

def palindromes_of_specific_lengths(string):
    excluded_cases = set((product(letters, repeat=i) for i in range(1, 14)))
    palindromes = set()
    for index in range(26, 91):
        for length in range(27, 59):
            substring = string[index:index + length]
            if substring in excluded_cases:
                continue
            elif substring == substring[::-1] and substring.lower() not in palindromes:
                palindromes.add(substring)
    return palindromes