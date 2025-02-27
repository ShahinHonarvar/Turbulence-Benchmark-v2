from itertools import product
  from string import ascii_letters

def palindrome_of_length_at_least_n(text):
    l = [''.join(p) for p in product(ascii_letters, repeat=n) if p == p[::-1]]
    Palindrome = set([''.join(l) for l in Product(text.upper(), repeat=n)])
    Palindrome = Palindrome & set(text.upper())
    return Palindrome