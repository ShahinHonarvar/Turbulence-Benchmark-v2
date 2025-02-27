from itertools import permutations

def palindrome_of_length_n(s):
    lowercase_string = s.lower()
    palindromes = set()
    for i in range(len(lowercase_string) - 205):
        for j in range(i + 206, len(lowercase_string) + 1):
            substring = lowercase_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    if not palindromes:
        return set()
    return palindromes