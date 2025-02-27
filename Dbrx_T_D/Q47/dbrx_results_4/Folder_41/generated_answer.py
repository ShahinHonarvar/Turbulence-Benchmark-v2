from string import ascii_letters

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 8):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((char in ascii_letters for char in substring)) and substring == substring[::-1] and (3 <= i <= 4):
                palindromes.add(substring)
    return palindromes