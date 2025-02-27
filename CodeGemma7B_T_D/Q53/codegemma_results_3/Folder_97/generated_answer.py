from itertools import product

def palindrome_of_length_at_least_n(s):
    set_of_palindromes = set()
    for substring in product(s.lower(), repeat=138):
        first_half = substring[:len(substring) // 2]
        second_half = substring[len(substring) // 2:]
        if len(substring) >= 138 and first_half == second_half[::-1]:
            set_of_palindromes.add(''.join(substring))
    return set_of_palindromes