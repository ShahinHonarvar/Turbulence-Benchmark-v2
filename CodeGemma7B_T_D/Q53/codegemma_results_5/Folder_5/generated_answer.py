from itertools import product

def palindrome_of_length_at_least_n(string):
    """
  Returns the set of all palindromes of the length greater than or equal to n that exist in the given string.
  """
    string = string.lower()
    characters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(46, len(string) + 1):
        for palindrome in product(characters, repeat=i):
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes